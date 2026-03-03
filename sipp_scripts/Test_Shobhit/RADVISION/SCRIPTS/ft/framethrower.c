#include "framethrower.ext"

/***********************************************************************
*
*     FUNCTION : main()
*
*	  Description   : This function is the entry point for Framethrower
*					  
*					  
*   Return Value  :   Return TRUE on succesful execution.
*                     exits if some exception arrives.
*
************************************************************************/
S32 main(S32 argc, S8 **argv)
{
  FILE *fp;
  U8 skip_next = 0, indx, file_name[MAX_FILE_NAME];
  pthread_t send_thread_id, recv_thread_id;
  S32 thread_ret,call_indx = 0;

  initialize_ft();
  strcpy((S8 *)file_name, "ft.cfg");

  // handle all the command line arguments
  for(indx=1;indx<argc;indx++)
  {
    if(('-' != argv[indx][0]) || ('\0' != argv[indx][2]))
    {
      printf("Invalid arguements passed. Expected command is\n");
      printf("\t\t ./FT [-l] [-f] [configuration file name] [-c <x minutes>] [-s <num_of_cycles>] \n");
      printf("OR\n\t\t ./FT [-f] [-c <x minutes>] [-s <num_of_cycles>] [configuration file name] [-l]\n");
      printf("OR\n\t\t ./FT [-s <num_of_cycles>] [-c <x minutes>] [-f] [configuration file name] [-l]\n");
      printf("OR\n\t\t ./FT [-c <x minutes>] [-f] [-s <num_of_cycles>] [configuration file name] [-l]\n");
      exit(0);
    }
    if(1 != skip_next)
    {
      skip_next=0;
    }

	/*Handle the options, if any, given in the command line*/
    switch(argv[indx][1])
    {
    case 'l':
      {
        /*Enables the logs*/
        log_flag = 1;
      }
      break;
    case 'f':
	  /*Name of the configuration file is specified with the -f option*/
      {
	    /*Check that the next argument is not NULL after -f*/
        if(argv[indx+1] == NULL)
        {
          printf("\nName of the configuration file is missing with -f option \n");         
          exit(0);
        }
        else
        {
          strcpy((S8 *)file_name,argv[indx+1]);
          indx++;
          skip_next = 1;
        }
      }
      break;
    case 'c':
		/*The time interval in minutes is provided with the -c option.
		   Counters are displayed periodically after this interval */
      {
        S8 a[10]; 
        if(argv[indx+1] == NULL)
        {
          printf("\nvalue for the counter display interval missing with -c option \n");          
          exit(0);
        }
        else
        {
          strcpy((S8 *)a,(S8 *)argv[indx+1]);
          var.ctr_disp_interval = atoi(a);
          LOG_PRINT("ctr_disp_interval = %d",var.ctr_disp_interval);
          indx++; 
          skip_next = 1;
        }
      }
      break;

      /*If -s option is provided, data for all the calls will be 
      started immedietly without waiting for the start message 
      from challenger
      */
    case 's':
      {
        /*Read the num_of_cycles for which the data will be sent*/
        S8 a[10]; 
		/*Check that the next arg. after -c is not NULL */
        if(argv[indx+1] == NULL)
        {
          printf("\nvalue for the Num of cycles is missing with -s option \n");          
          exit(0);
        }
        else
        {
          strcpy((S8 *)a,(S8 *)argv[indx+1]);
          var.num_of_cycles = atoi(a);
          var.start_immediate_data = 1;
          LOG_PRINT("num_of_cycles = %d",var.num_of_cycles);
          indx++; 
          skip_next = 1;

          /*Mark all the calls as valid for sending data*/
          for(call_indx=0; call_indx < MAX_NUM_CALLS; call_indx++)
          {
            call_info[call_indx].is_valid = FT_TRUE;
          }
        }
      }
      break;

    default:
      {
        printf("Invalid arguements passed. Expected command is\n");
        printf("\t\t ./FT [-l] [-f] [configuration file name] [-c <x minutes>] [-s <num_of_cycles>] \n");
        printf("OR\n\t\t ./FT [-f] [-c <x minutes>] [-s <num_of_cycles>] [configuration file name] [-l]\n");
        printf("OR\n\t\t ./FT [-s <num_of_cycles>] [-c <x minutes>] [-f] [configuration file name] [-l]\n");
        printf("OR\n\t\t ./FT [-c <x minutes>] [-f] [-s <num_of_cycles>] [configuration file name] [-l]\n");
        exit(0);
      }
      break;
    }    
  }

  /*Open the configuration file to read the configuration parameters*/
  if((fp = fopen((S8 *)file_name, "r")) == NULL)
  {
    printf("Cannot open file %s \n", file_name);
    exit(0);
  }
  else
  {
    //Read the configuration file and save the information in static variables.
    read_config(fp);
    fclose(fp);
    if(EXIT_FAILURE == validate_params(PACKET_TYPE_RTP))
    {
      printf("Correct the above mentioned values and then restart again\n");
      exit(EXIT_FAILURE);
    }
    //Copy the packet related information in the call contexts.
    update_call_info(PACKET_TYPE_RTP);
    open_aoip_ft_ports();

    // initially to check the link between FT and ETPC
    send_ping_message(PACKET_TYPE_RTP);

    /* Create two threads, one for sending and other for receiving 
    the packets */
    thread_ret = pthread_create( &recv_thread_id, NULL, aoip_recv_routine,"RecvThread");
    if(thread_ret != 0)
    {
      LOG_PRINT("recv_thread creation failed with error %d",thread_ret);
      exit(0);
    }

    thread_ret = pthread_create( &send_thread_id, NULL, aoip_send_routine,"SendThread");
    if(thread_ret != 0)
    {
      LOG_PRINT("send_thread creation failed with error %d",thread_ret);
      exit(0);
    }

    printf("\n\t ---------- FT started ---------- \n");

    while(1)
    {      
      display_counters();

      /*Sleep for ctr_disp_interval time before printing the 
	    counter values for the next time.Meanwhile counters are getting 
		incremented in the send and recv thread routines.*/

      usleep((var.ctr_disp_interval * 60 * 50 * CYCLE_INTERVAL) * 1000);      
    }

    pthread_join(send_thread_id,NULL);
    pthread_join(recv_thread_id,NULL);
  }/*End else*/

  return(FT_TRUE);

}/*End of function main*/





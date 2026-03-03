#include "framethrower.ext"


#include "framethrower.ext"

/*********************************************************************
*
*   Function      :   pater_send_routine
*   Description   :   This function sends packets for all the calls through 
*                     pater_framethrower after a period of 20ms 
*                     i.e one cycle interval.
*					  
*					  If delay value is also provided,then packets 
*					  are sent after delay number of cycles.
*   Return Value  :   None
*
**********************************************************************/
void *pater_send_routine()
{
  struct timeb tp;
  U32 init_time = 0, end_time = 0;  //To implement the 20ms interval   
  U32 cycle_num = 0;  //Used to keep track of how many cycles have been sent
  U32 rand_intrvl,var_time;
  U32 cycles_sent;

  ftime(&tp);
  init_time = (tp.time)*1000 + tp.millitm;
  end_time = init_time;  
  cycles_sent = var.num_of_cycles;

  var_time = time(NULL);
  srand(var_time);

  while(1)
  {
    if((var.start_immediate_data == 0) || (var.num_of_cycles >= 0))
    {
      ftime(&tp);
      end_time = (tp.time)*1000 + tp.millitm;
      if(CYCLE_INTERVAL < end_time - init_time)
      {
        init_time = end_time;      
      }
      else
      {
       if((cycle_num >= var.start_err_pkt)  && (cycle_num < var.end_err_pkt))
       {
        rand_intrvl = rand();
        rand_intrvl = rand_intrvl % 10;
       // LOG_PRINT("\nrand:%d",rand_intrvl);  
        usleep(((CYCLE_INTERVAL * var.set_delay + (CYCLE_INTERVAL - rand_intrvl)) - (end_time - init_time)) * 1000);
        init_time += (CYCLE_INTERVAL * var.set_delay + (CYCLE_INTERVAL - rand_intrvl));
       }
       
       else
       {
        usleep(((CYCLE_INTERVAL * var.set_delay + CYCLE_INTERVAL) - (end_time - init_time)) * 1000);
        init_time += (CYCLE_INTERVAL * var.set_delay + CYCLE_INTERVAL);
      }
      } 

			//printf("\nsending this cycle at:%lu",(end_time));
      pater_send_packets();
      cycle_num++;

      /*This is used only in case of -s option so 
       that packets are sent in the specified num of cycles.*/
      if(0 < var.num_of_cycles)
      {
        var.num_of_cycles--;
        if(0 == var.num_of_cycles)
        {
          LOG_PRINT("\n Number of cycles for which Packets has been sent for all configured calls :%u \n", cycles_sent);
          display_counters();
          exit(0);
        }
      }
    }
  }/*End of while(1)*/
}

/*********************************************************************
*
*   Function      :   aoip_send_routine
*   Description   :   This function sends packets for all the calls through 
*                     aoip_framethrower after a period of 20ms 
*                     i.e one cycle interval.
*					  
*					  If delay value is also provided,then packets 
*					  are sent after delay number of cycles.
*   Return Value  :   None 
*                   
**********************************************************************/
void *aoip_send_routine()
{
  struct timeb tp;
  U32 init_time = 0, end_time = 0;  //To implement the 20ms interval   
  U32 cycles_sent;
  U32 cycle_num = 0;  //Used to keep track of how many cycles have been sent
  U32 rand_intrvl,var_time;

  ftime(&tp);
  init_time = (tp.time)*1000 + tp.millitm;
  end_time = init_time; 
  cycles_sent = var.num_of_cycles;

  var_time = time(NULL);
  srand(var_time);

  while(1)
  {    
    if((var.start_immediate_data == 0) || (var.num_of_cycles >= 0))
    {
      ftime(&tp);
      end_time = (tp.time)*1000 + tp.millitm;
      if(CYCLE_INTERVAL < end_time - init_time)
      {
        init_time = end_time;      
      }
      else
      {
       if((cycle_num >= var.start_err_pkt) &&(cycle_num < var.end_err_pkt))
       {
        rand_intrvl = rand();
        rand_intrvl = rand_intrvl % 10;
        //LOG_PRINT("\nrand:%d",rand_intrvl);  
        usleep(((CYCLE_INTERVAL * var.set_delay + (CYCLE_INTERVAL - rand_intrvl)) - (end_time - init_time)) * 1000);
        init_time += (CYCLE_INTERVAL * var.set_delay + (CYCLE_INTERVAL - rand_intrvl));
       }
       else
       {
        usleep(((CYCLE_INTERVAL * var.set_delay + CYCLE_INTERVAL) - (end_time - init_time)) * 1000);
        init_time += (CYCLE_INTERVAL * var.set_delay + CYCLE_INTERVAL);
      }
      }
      //LOG_PRINT("\nsending this cycle at:%lu",(init_time));
      aoip_send_packets();    
      cycle_num++;
      
      if(0 < var.num_of_cycles)
      {
        var.num_of_cycles--;
        if(0 == var.num_of_cycles)
        {
          LOG_PRINT("\n Number of cycles for which Packets has been sent for all configured calls :%u \n", cycles_sent);
          display_counters();
          exit(0);
        }
      }	  
    }
  }/*End of while(1)*/
}

/*********************************************************************
*
*   Function      :   pater_recv_routine
*   Description   :   This function receives the packets at pater_framethrower
*                
*   Return Value  :   None
*
**********************************************************************/

void *pater_recv_routine()
{
  U16 call_index = 0, seq_no = 0;
  S32 len = -1;
  struct sockaddr_in address;
  U32 a_len = sizeof (struct sockaddr_in);
  U8 *ptemp = NULL, rec_buf[MAX_PACKET_SIZE] = {'\0'};  

  while(1)
  {
    if ((len = recvfrom(call_info[MAX_NUM_CALLS].call_config.pater_ft_fd, rec_buf,
      MAX_PACKET_SIZE, MSG_DONTWAIT, (struct sockaddr *)&address,&a_len)) > 0)
    {
      var.num_of_pkts_recvd++;
      len -= IPV4_HDR_LENGTH + UDP_HDR_LENGTH;
      ptemp = rec_buf + IPV4_HDR_LENGTH + UDP_HDR_LENGTH;
      seq_no = rec_buf[IPV4_HDR_LENGTH + UDP_HDR_LENGTH];  //  first byte is the sequence number in RTPC

      //  All packets are received at port 65534 at PATER FT. 
      //  Hence, call_index is extracted from the source port
      call_index = (ntohs(address.sin_port) - ETPC_FIRST_CALL_PORT) / 2;
call_index = call_index - var.base_call_index;
       if(MAX_NUM_CALLS < call_index)
          {
                  LOG_PRINT("\n Invalid call received to PATER\n");
                  continue;
          }

      LOG_PRINT("\n RECEIVED RTPC PACKET \n");
      LOG_PRINT(" RTP seq no: %u \n",seq_no);
      LOG_PRINT(" \n No of Bytes received : %u for call number:%u \n", len, (call_index + var.base_call_index));      
      print_rtpc_packet(ptemp,len);

      //validate the sequence number and contents of the packet
      validate_packet(call_index, rec_buf + IPV4_HDR_LENGTH + UDP_HDR_LENGTH, len, PACKET_TYPE_RTPC, seq_no);        
    }

    if(1 != var.start_immediate_data)
    {
      listen_challenger_port(PACKET_TYPE_RTPC);
    }
  }
}

/*********************************************************************
*
*   Function      :   aoip_recv_routine
*   Description   :   This function receives the packets at aoip_framethrower
*   Return Value  :   None
*
**********************************************************************/

void *aoip_recv_routine()
{
  U16 call_index = 0, seq_no = 0;
  S32 len = -1;
  struct sockaddr_in address;
  U32 a_len = sizeof (struct sockaddr_in);
  U8 *ptemp = NULL;
  U8 rec_buf[MAX_PACKET_SIZE] = {'\0'};

  while(1)
  {
    for(call_index = 0; call_index < MAX_NUM_CALLS; call_index++)
    {      
      if ((len = recvfrom(call_info[call_index].call_config.aoip_ft_fd, rec_buf,
        MAX_PACKET_SIZE, MSG_DONTWAIT, (struct sockaddr *)&address,&a_len)) > 0)
      {
        var.num_of_pkts_recvd++;
        ptemp = rec_buf;
        seq_no = ((U16)(rec_buf[2] << 8)) | rec_buf[3];

        LOG_PRINT("\n RECEIVED RTP PACKET \n");
        LOG_PRINT(" RTP seq no: %u \n",seq_no);
        LOG_PRINT(" \n No of Bytes received : %u for call number:%u \n", len, (call_index + var.base_call_index));                
        print_rtp_packet(ptemp,len);

        //validate the sequence number and contents of the packet
        validate_packet(call_index, rec_buf, len, PACKET_TYPE_RTP, seq_no);
      }
    }

    if(1 != var.start_immediate_data)
    {
      listen_challenger_port(PACKET_TYPE_RTP);    
    }
  }
}

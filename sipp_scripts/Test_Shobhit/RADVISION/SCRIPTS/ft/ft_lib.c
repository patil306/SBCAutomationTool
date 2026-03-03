#include "framethrower.ext"

/***************************************************************
*
*     FUNCTION : print_rtpc_packet()
*
****************************************************************/

void print_rtpc_packet(U8 *p,S32 length)
{

  rtpc_t rtp_packet = {0};
  S32 payload_length=0;

  rtp_packet.seq_no = (*p & 0xFF);
  p++;
  LOG_PRINT(" RTPC SEQUENCE NUMBER = %d \n",rtp_packet.seq_no);

  rtp_packet.ts = ((*p & 0xFF)<<8);
  p++;
  rtp_packet.ts|=(*p & 0xFF);
  p++;
  LOG_PRINT(" RTPC TIMESTAMP = %d \n",rtp_packet.ts);

  rtp_packet.m_bit = ((*p >>7) & 0x01);
  LOG_PRINT(" M_BIT = %d \n",rtp_packet.m_bit);
  rtp_packet.payload = (*p & 0x7F);
  p++;
  LOG_PRINT(" PAYLOAD = %d \n",rtp_packet.payload);

  payload_length = length - RTPC_HEADER_LENGTH;

  hexdump_payload(&p,payload_length);

  LOG_PRINT("\n");
} /* function print_rtp_packet_ends */




/***************************************************************
*
*     FUNCTION : print_rtp_packet()
*
****************************************************************/
void print_rtp_packet(U8 *p,S32 length)
{

  rtp_t rtp_packet = {0};
  S32 payload_length=0;
  S32 cc = 0 ;

  rtp_packet.version = (*p >> 6)&0x03;
  LOG_PRINT(" VERSION = %d \n",rtp_packet.version);

  rtp_packet.padding = (*p >> 5)&0x01;
  LOG_PRINT(" PADDING = %d \n",rtp_packet.padding);

  rtp_packet.x_bit = ((*p >>4) & 0x01);
  LOG_PRINT(" X_BIT = %d \n",rtp_packet.x_bit);

  rtp_packet.cc = (*p & 0x0F);
  p++;
  LOG_PRINT(" CSRC COUNT (CSRC) = %d\n",rtp_packet.cc);

  rtp_packet.m_bit = ((*p >>7) & 0x01);
  LOG_PRINT(" M_BIT = %d \n",rtp_packet.m_bit);

  rtp_packet.payload = (*p & 0x7F);
  p++;
  LOG_PRINT(" PAYLOAD = %d \n",rtp_packet.payload);

  rtp_packet.seq_no = ((*p & 0xFF)<<8);
  p++;
  rtp_packet.seq_no|=(*p & 0xFF);
  p++;
  LOG_PRINT(" RTP SEQUENCE NUMBER = %d \n",rtp_packet.seq_no);
  rtp_packet.ts = ((*p & 0xFF)<<24);
  p++;
  rtp_packet.ts |= ((*p & 0xFF)<<16);
  p++;
  rtp_packet.ts |= ((*p & 0xFF)<<8);
  p++;
  rtp_packet.ts |=(*p & 0xFF);
  p++;
  LOG_PRINT(" RTP TIMESTAMP = %u \n",rtp_packet.ts);

  rtp_packet.ssrc = ((*p & 0xFF)<<24);
  p++;
  rtp_packet.ssrc |= ((*p & 0xFF)<<16);
  p++;
  rtp_packet.ssrc |= ((*p & 0xFF)<<8);
  p++;
  rtp_packet.ssrc |=(*p & 0xFF);
  p++;
  LOG_PRINT(" SSRC = %u \n",rtp_packet.ssrc);
  while(cc < rtp_packet.cc)
  {
    rtp_packet.csrc[cc] = ((*p & 0xFF)<<24);
    p++;
    rtp_packet.csrc[cc] |= ((*p & 0xFF)<<16);
    p++;
    rtp_packet.csrc[cc] |= ((*p & 0xFF)<<8);
    p++;
    rtp_packet.csrc[cc] |=(*p & 0xFF);
    p++;
    LOG_PRINT(" CSRC[%d] = %u \n",cc,rtp_packet.csrc[cc]);
    cc++;
  }

  payload_length = length - (RTP_HEADER_LENGTH(rtp_packet.cc));

  hexdump_payload(&p,payload_length);

  LOG_PRINT("\n");
} /* function print_rtp_packet_ends */


/**************************************************************
*
*      FUNCTION : hexdump_payload()
*
***************************************************************/
void hexdump_payload(U8 **p,S32 length)
{

  S32 i=0;
  for(i = 0; i<length; i++)
  {
    if(i%8 == 0)
      LOG_PRINT("\n");
    LOG_PRINT(" %.2x\t",**p);
    (*p)++;
  }

  LOG_PRINT("\n");

}

/*********************************************************************
*
*   Function      :   pater_send_packets
*   Description   :   This function sends packets for all the calls
*   Return Value  :   Returns "error_flag".
*                       error_flag = 0 means no error
*                       error_flag = 1 means error
*
**********************************************************************/
U8 pater_send_packets(void)
{
	U16 call_index = 0;
  U8 error_flag = EXIT_SUCCESS;

  for(call_index=0; call_index<MAX_NUM_CALLS; call_index++)
  {
    if(call_info[call_index].is_valid == FT_TRUE)
    {
			if(call_info[call_index].call_config.hscsd_no_of_port == 1) 
        {
				error_flag = send_pkt_single_group(call_index);
        }

			else if(call_info[call_index].call_config.hscsd_no_of_port > 1)
        {
				if(call_info[call_index].call_config.packet_group == PKT_GRP_SINGLE)             
          { 
					error_flag = send_pkt_single_group(call_index);
            }
				else if(call_info[call_index].call_config.packet_group == PKT_GRP_MULTI)
            {
						error_flag = send_pkt_multi_group(call_index);
            }
          }
    }
  }

  return error_flag;
}/*End of pater_send_packets*/

/*********************************************************************
*
*   Function      :   aoip_send_packets
*   Description   :   This function sends packets for all the calls
*   Return Value  :   Returns "error_flag".
*                       error_flag = 0 means no error
*                       error_flag = 1 means error
*
**********************************************************************/
U8 aoip_send_packets(void)
{

  U16 call_index = 0, packet_index = 0;
  S32 length = 0,indx;
  U8 error_flag = EXIT_SUCCESS;

  for(call_index=0; call_index<MAX_NUM_CALLS; call_index++)
  {
    if(call_info[call_index].is_valid == FT_TRUE)
    {
      /*curr_pkt_indx is used to keep track 
				of the pkt indx sent in the previous cycle
      */

				indx = call_info[call_index].packet_grp[0].curr_pkt_indx;
      if(call_info[call_index].call_config.sbc_port != '\0')
      {
					if(('\0' == call_info[call_index].packet_grp[0].packet_ref[indx].packet_no) || (call_info[call_index].packet_grp[0].curr_pkt_indx == MAX_RTP_PKT_PER_CALL/2))
        {
						call_info[call_index].packet_grp[0].curr_pkt_indx = 0;
						indx = call_info[call_index].packet_grp[0].curr_pkt_indx;					    }       
					if('\0' != call_info[call_index].packet_grp[0].packet_ref[indx].packet_no)
        {
						packet_index = call_info[call_index].packet_grp[0].packet_ref[indx].packet_no;
						if((call_info[call_index].packet_grp[0].packet_ref[indx].skip == 0) || (call_info[call_index].packet_grp[0].packet_ref[indx].skip_after_cycle > 0))
          { 
            length = (RTP_HEADER_LENGTH(packet_info[packet_index].pkt_hdr.rtp_hdr.cc)) + packet_info[packet_index].pkt_hdr.rtp_hdr.length;
							LOG_PRINT("\nsending packet no:%d for call_id:%d:\n",call_info[call_index].packet_grp[0].packet_ref[indx].packet_no,call_index+var.base_call_index);
            error_flag = send_rtp_packet(length, call_index, packet_index);
            //Increment the seq no. for this call
            
             if(0xFFFF <= call_info[call_index].rtp_seq_no)
             { 
               call_info[call_index].rtp_seq_no = 0;
             }
            call_info[call_index].rtp_seq_no++;
							call_info[call_index].packet_grp[0].packet_ref[indx].skip_after_cycle--;
							call_info[call_index].packet_grp[0].curr_pkt_indx++;
          }
          else
          {
            LOG_PRINT("skipping packet id:%d",packet_index);

            /*Seq no. will be incremented even if the packet is skipped*/
            call_info[call_index].rtp_seq_no++;
							call_info[call_index].packet_grp[0].curr_pkt_indx++;
							call_info[call_index].packet_grp[0].packet_ref[indx].skip--;
          }

        }
      }/*End of if(call_info...etpc_port !=0 */
    }
  }

  return error_flag;
}

/**********************************************************
*
*   FUNCTION : check_string
*
***********************************************************/

S32 check_string(S8 *str)
{
  token[0] = '\0';
  sscanf(str,"%s",token);
  if(str[0] == '\n'||token[0] == '#' || token[0] == '\0')
    return 1;
  else
    return 0;
}




/*********************************************************************
*
*   Function      :   initialize_ft
*   Description   :   This function initializes all the global variables
*                     i.e. config, call and packet variables
*
**********************************************************************/


void initialize_ft(void)
{
  U16 call_index = 0;

  //Global variables
  log_flag = 0;

  //Config variable
  memset(&var, '\0', sizeof(variable_str));
  var.challenger_port = 0xffff;
  var.ctr_disp_interval = 0xf;

  //Call related parameters
  memset(call_info, '\0', (sizeof(call_info_t) * MAX_NUM_CALLS));
  for(call_index=0; call_index < MAX_NUM_CALLS; call_index++)
  {
    call_info[call_index].is_valid = FT_FALSE;
    call_info[call_index].call_config.hscsd_no_of_port = 1;
  }

  //Packet related parameters
  memset(packet_info, '\0', (sizeof(packet_t) * MAX_RTP_PACKETS));

  call_info[MAX_NUM_CALLS].call_config.pater_ft_port[0] = ETPA_RECEPTION_PORT;

  //ext variables  
  memset(first_packet_recvd, FT_FALSE, (sizeof(U8) * MAX_NUM_CALLS));

  return;
}


/*********************************************************************
*
*   Function      :   validate_params
*   Description   :   This function validates values of parameters
*                     read from the configuration file
*   Return Value  :   Returns "error_flag".
*                       error_flag = 0 means no error
*                       error_flag = 1 means error
* 
**********************************************************************/
U8 validate_params(U32 packet_type)
{
  S32 indx = 0;
  S32 error_flag = EXIT_SUCCESS;
  S32 port_var = 0;
  packet_t temp;
  memset(&temp, 0, sizeof(packet_t));

  //Config variable   
  if((0 > var.set_delay) || (0xFFFF < var.set_delay))
  {
    printf("Invalid SET_DELAY VALUE, entered delay = %u \n", var.set_delay);
    error_flag = EXIT_FAILURE;
  }

  if((0 > var.ts_delay) || ( 0xFFFF < var.ts_delay))
  {
    printf(" Invalid TIMESTAMP_DELAY VALUE, entered delay = %u \n", var.ts_delay);
    error_flag = EXIT_FAILURE;
  }

  for(indx=0;indx<MAX_NUM_CALLS;indx++)
  {
    if('\0' != call_info[indx].call_config.sbc_port)
    {
      if((0 > (indx + var.base_call_index)) || (MAX_CALL_ID <= (indx + var.base_call_index)))
      {
        printf(" Sum of base_call_index[%hu] and call_index[%u] is more than maximum allowed %u \n", var.base_call_index, indx, MAX_CALL_ID);
        error_flag = EXIT_FAILURE;
      }
			if((call_info[indx].call_config.hscsd_no_of_port > HSCSD_NUM_OF_PORTS) && (call_info[indx].call_config.hscsd_no_of_port < 0))
      {
				printf("\n Invalid number of hscsd port,Maximum and Minimum number of port allowed is 4 and 0 given number of port is %d \n",call_info[indx].call_config.hscsd_no_of_port);
        error_flag = EXIT_FAILURE;
      }
			if(call_info[indx].call_config.hscsd_no_of_port == 0)
			{
				LOG_PRINT("\n Number of HSCSD port is ZERO thus setting it to default value, 1\n");
				call_info[indx].call_config.hscsd_no_of_port = 1; 
			}
      for(port_var = 0; port_var < HSCSD_NUM_OF_PORTS;port_var++)
	  {
          if((0 > call_info[indx].call_config.pater_ft_port[port_var]) || (0xFFFF < call_info[indx].call_config.pater_ft_port[port_var]))
      {
            printf("Invalid PATER_FT_PORT value=%hu, for call_index=%u \n", call_info[indx].call_config.pater_ft_port[port_var], indx);
        error_flag = EXIT_FAILURE;
      }
	  }
      if((0 > call_info[indx].call_config.ft_port) || (0xFFFF < call_info[indx].call_config.ft_port))
      {
        printf("Invalid FT_PORT value=%hu, for call_index=%u \n", call_info[indx].call_config.ft_port, indx);
        error_flag = EXIT_FAILURE;
      }


      if((0 > call_info[indx].call_config.sbc_port) || (0xFFFF < call_info[indx].call_config.sbc_port))
      {
        printf("Invalid SBC_PORT value=%hu, for call_index=%u \n", call_info[indx].call_config.sbc_port, indx);
        error_flag = EXIT_FAILURE;
      }

      if(PACKET_TYPE_RTPC == packet_type)
      {
				/*If num of ports is set to 1, there will be a single channel to send data.
				Thus packet group is set to SINGLE always.*/

				if(1 == call_info[indx].call_config.hscsd_no_of_port)
				{
					call_info[indx].call_config.packet_group = PKT_GRP_SINGLE;
				}
        if((0 > call_info[indx].init_seq_num) || (0xFF < call_info[indx].init_seq_num))
        {
          printf("Invalid SEQ_NUM value=%u, for call_index=%u \n", call_info[indx].init_seq_num, indx);
          error_flag = EXIT_FAILURE;
        }
      }
      else if(PACKET_TYPE_RTP == packet_type)
      {
				/* In AoIP HSCSD is not valid i.e there will be a single PACKET_REF and a single                                      channel thus packet group is always SINGLE. */

				call_info[indx].call_config.packet_group = PKT_GRP_SINGLE;

        if((0 > call_info[indx].init_seq_num) || (0xFFFF < call_info[indx].init_seq_num))
        {
          printf("Invalid SEQ_NUM value=%u, for call_index=%u \n", call_info[indx].init_seq_num, indx);
          error_flag = EXIT_FAILURE;
        }
      }
    }
  }

  for(indx=0;indx<MAX_RTP_PACKETS;indx++)
  {
    if(PACKET_TYPE_RTPC == packet_info[indx].packet_type)
    {
      //validation of RTPC packets
      if(0 != memcmp(&packet_info[indx], &temp, sizeof(packet_t)))
      {
        if((0 > packet_info[indx].pkt_hdr.rtpc_hdr.length) || (40 < packet_info[indx].pkt_hdr.rtpc_hdr.length))
        {
          printf("Invalid RTPC Header LENGTH=%u for index=%u \n", packet_info[indx].pkt_hdr.rtpc_hdr.length, indx);
          error_flag = EXIT_FAILURE;
        }

        if(!((0 <= packet_info[indx].pkt_hdr.rtpc_hdr.ts) && (0xFFFFFFFF > packet_info[indx].pkt_hdr.rtpc_hdr.ts)))
        {
          printf("Invalid TIMESTAMP VALUE[%u] for index=%u \n", packet_info[indx].pkt_hdr.rtpc_hdr.ts, indx);
          error_flag = EXIT_FAILURE;
        }

        if(!((0 == packet_info[indx].pkt_hdr.rtpc_hdr.m_bit) || (1 == packet_info[indx].pkt_hdr.rtpc_hdr.m_bit)))
        {
          printf("Invalid M_BIT value[%u] for index%u \n", packet_info[indx].pkt_hdr.rtpc_hdr.m_bit, indx);
          error_flag = EXIT_FAILURE;
        }

        switch(packet_info[indx].pkt_hdr.rtpc_hdr.payload)
        {
        case G711_U_LAW:
        case CSD_TRAU_FRAME:
        case GSM_FR_CODEC:
        case G711_A_LAW:
        case GSM_EFR_CODEC:
        case GSM_HR_CODEC:
        case AMR_FR_CODEC:
        case AMR_WB_CODEC:
        case CLEAR_MODE:
          break;
        default:
          {
            printf("Invalid PAYLOAD value: %u for index=%u \n" , packet_info[indx].pkt_hdr.rtpc_hdr.payload, indx);
            error_flag = EXIT_FAILURE;
          }
          break;
        }

        if((0 > packet_info[indx].expected_packet_length) || (160 < packet_info[indx].expected_packet_length))
        {
          printf("Invalid Expected Packet Length=%u for index=%u \n", packet_info[indx].expected_packet_length, indx);
          error_flag = EXIT_FAILURE;
        }
      }
    }
    else if(PACKET_TYPE_RTP == packet_info[indx].packet_type)
    {
      //validation of RTP packets
      if(0 != memcmp(&packet_info[indx], &temp, sizeof(packet_t)))
      {
        if((0 > packet_info[indx].pkt_hdr.rtp_hdr.length) || (160 < packet_info[indx].pkt_hdr.rtp_hdr.length))
        {
          printf("Invalid RTP Header LENGTH=%u for index=%u \n", packet_info[indx].pkt_hdr.rtp_hdr.length, indx);
          error_flag = EXIT_FAILURE;
        }

        if(!((0 <= packet_info[indx].pkt_hdr.rtp_hdr.ts) && (0xFFFFFFFF > packet_info[indx].pkt_hdr.rtp_hdr.ts)))
        {
          printf("Invalid TIMESTAMP VALUE[%u] for index=%u \n", packet_info[indx].pkt_hdr.rtp_hdr.ts, indx);
          error_flag = EXIT_FAILURE;
        }

        if(!((0 == packet_info[indx].pkt_hdr.rtp_hdr.m_bit) || (1 == packet_info[indx].pkt_hdr.rtp_hdr.m_bit)))
        {
          printf("Invalid M_BIT value[%u] for index%u \n", packet_info[indx].pkt_hdr.rtp_hdr.m_bit, indx);
          error_flag = EXIT_FAILURE;
        }
        switch(packet_info[indx].pkt_hdr.rtp_hdr.payload)
        {
        case G711_U_LAW:
        case CSD_TRAU_FRAME:
        case GSM_FR_CODEC:
        case G711_A_LAW:
        case GSM_EFR_CODEC:
        case GSM_HR_CODEC:
        case AMR_FR_CODEC:
        case AMR_WB_CODEC:
        case CLEAR_MODE:
          break;
        default:
          {
            printf("Invalid PAYLOAD value: %u for index=%u \n" , packet_info[indx].pkt_hdr.rtp_hdr.payload, indx);
            error_flag = EXIT_FAILURE;
          }
          break;
        }

        if(2 != packet_info[indx].pkt_hdr.rtp_hdr.version)
        {
          printf("Invalid VERSION value%u for index=%u \n" , packet_info[indx].pkt_hdr.rtp_hdr.version,indx);
          error_flag = EXIT_FAILURE;
        }

        if((0 != packet_info[indx].pkt_hdr.rtp_hdr.padding) && (1 != packet_info[indx].pkt_hdr.rtp_hdr.padding))
        {
          printf("Invalid PADDING value%u for index=%u \n" , packet_info[indx].pkt_hdr.rtp_hdr.padding,indx);
          error_flag = EXIT_FAILURE;
        }
        if((0 != packet_info[indx].pkt_hdr.rtp_hdr.x_bit) && (1 != packet_info[indx].pkt_hdr.rtp_hdr.x_bit))
        {
          printf("Invalid X_BIT value%u for index=%u \n" , packet_info[indx].pkt_hdr.rtp_hdr.x_bit,indx);
          error_flag = EXIT_FAILURE;
        }

        if((0 > packet_info[indx].pkt_hdr.rtp_hdr.cc) || (15 < packet_info[indx].pkt_hdr.rtp_hdr.cc))
        {
          printf("Invalid CSRC value%u for index=%u\n" , packet_info[indx].pkt_hdr.rtp_hdr.cc,indx);
          error_flag = EXIT_FAILURE;
        }

        if((0 > packet_info[indx].expected_packet_length) || (40 < packet_info[indx].expected_packet_length))
        {
          printf("Invalid Expected Packet Length=%u for index=%u \n", packet_info[indx].expected_packet_length, indx);
          error_flag = EXIT_FAILURE;
        }
      }
    }
    else if(0 != packet_info[indx].packet_type)
    {
      printf("Invalid packet type[%u] for index=%u \n", packet_info[indx].packet_type, indx);
      error_flag = EXIT_FAILURE;
    }
  }

  return error_flag;
}

/*********************************************************************
*
*   Function      :   update_call_info 
*   Description   :   This function updates the packet skip information 
*                     and initial seq_no in each call.
*   Return Value  :   None 
**********************************************************************/

void update_call_info(U32 packet_type)
{
  U32 call_indx = 0, pkt_indx = 0, indx = 0, packet_no = 0, num = 0;
  U32 ctr = 0; /*At the end of the loop,it points to the
               index of the first Invalid pkt
               (RTPC for AoIP RTP for P-Ater) in the ref list */  

  for(call_indx=0; call_indx<MAX_NUM_CALLS; call_indx++)
  {
    U32 expected_pkt_indx = 0;

    for(pkt_indx=0; pkt_indx<MAX_RTP_PKT_PER_CALL; pkt_indx++)
    {
      ctr = pkt_indx;
			/*	 Call information for all the packet means packet_ref_1, 
			packet_ref_2,packet_ref_3 and packet_ref_4 will be same.
			So we have used channel number 1 to update the call info.
			*/
			if('\0' != call_info[call_indx].packet_grp[0].packet_ref[pkt_indx].packet_no)
      {
				packet_no = call_info[call_indx].packet_grp[0].packet_ref[pkt_indx].packet_no;

        /* Remove all the packets which are not of RTP type from packet_ref of the calls for AoIP FT */
        if(!(packet_info[packet_no].packet_type == packet_type))
        { 
          if((MAX_RTP_PKT_PER_CALL/2) > expected_pkt_indx)
          {
          call_info[call_indx].expected_packet_ref[expected_pkt_indx++] = packet_no;
          }
 
          for(indx=pkt_indx +1; indx<MAX_RTP_PKT_PER_CALL;)
          {
						if('\0' != call_info[call_indx].packet_grp[0].packet_ref[indx].packet_no)
            {
							num = call_info[call_indx].packet_grp[0].packet_ref[indx].packet_no; 

              /* Check if the next packet is a valid entry
              and replace the invalid pkt with this pkt else move to find the next valid pkt */
              if(packet_info[num].packet_type == packet_type)
              {
								call_info[call_indx].packet_grp[0].packet_ref[ctr].packet_no = num;
								call_info[call_indx].packet_grp[0].packet_ref[ctr].skip = packet_info[num].skip;
								call_info[call_indx].packet_grp[0].packet_ref[ctr].skip_after_cycle = packet_info[num].skip_after_cycle;
                indx++;
                ctr++;   /*ctr points to the index next to a valid entry*/ 
              }
              else
              {
               if((MAX_RTP_PKT_PER_CALL/2) > expected_pkt_indx)
	       {
               call_info[call_indx].expected_packet_ref[expected_pkt_indx++] = num;
                indx++;
	       }	
              }
            }
            /*Set all the invalid packets to zero when 
            the reference list contains less than Max no of pkts */
            else
            {
              /* ctr gives the first invalid entry */
              for(ctr=ctr;ctr<MAX_RTP_PKT_PER_CALL;ctr++)
              {
								call_info[call_indx].packet_grp[0].packet_ref[ctr].packet_no = '\0';
              }
              break;          
            }
          }

          /*Set all the invalid packets to zero when 
          the reference list contains Max. no. of packets.
          ctr gives the first invalid entry. */ 
          for(ctr=ctr;ctr<MAX_RTP_PKT_PER_CALL;ctr++)
          {
						call_info[call_indx].packet_grp[0].packet_ref[ctr].packet_no = '\0';
          }
        }
        else
        {
					call_info[call_indx].packet_grp[0].packet_ref[pkt_indx].skip = packet_info[packet_no].skip;
					call_info[call_indx].packet_grp[0].packet_ref[pkt_indx].skip_after_cycle = packet_info[packet_no].skip_after_cycle;
        }
      }/*End of if()call_info[call_ind]...*/
    }/* End of for(pkt_indx=0;..*/ 
  }/* End of for(call_indx=0;.. */
}/*End of function update_call_info*/

void display_counters()
{
  printf("\n----------COUNTERS--------------------  \n");
  printf("Number of packets sent = %llu \n", var.num_of_pkts_sent);
  printf("Number of packets received = %llu \n", var.num_of_pkts_recvd);
  printf("Number of out of sequence packets = %llu \n", var.num_of_out_of_seq_pkts);
  printf("Number of corrupted packets = %llu \n", var.num_of_corrupt_pkts);
  printf("----------------------------------------  \n");

  return;
}

/*********************************************************************
*
*   Function      :   validate_packet
*   Description   :   This function validates the sequence number and 
*                     content of the received packets  
*
*   Return Value  :   Void
**********************************************************************/

void validate_packet(S32 call_index, U8 *buffer, S32 len, S32 ft_type, U16 seq_no)
{
  validate_packet_sequence_number(call_index, buffer, len, ft_type, seq_no);
  validate_packet_contents(call_index, buffer, len, ft_type, seq_no);

  return;
}

void validate_packet_sequence_number(S32 call_indx, U8 *buffer, S32 len, S32 ft_type, U16 seq_no)
{
  U16 pkt_indx = 0, indx = 0;

  if(FT_FALSE == first_packet_recvd[call_indx])
  {
    for(indx=0;indx<MAX_RTP_PKT_PER_CALL/2;indx++)
    {
      pkt_indx = call_info[call_indx].expected_packet_ref[indx];

      if(('\0' != pkt_indx) && ('\0' != packet_info[pkt_indx].packet_type))
      {
        call_info[call_indx].last_recvd_seq_num = seq_no;
        first_packet_recvd[call_indx] = FT_TRUE;
      }
      break;
    }
  }
  else
  {
    /*At Ater side, seq_no is of 1 Byte therefore after seq_no
      255 is received, next expected packet is with seq_no 0
     */

    if(ft_type == PACKET_TYPE_RTPC)
    {
     if((call_info[call_indx].last_recvd_seq_num + 1) >= 0xFF)
     {
      if(seq_no != 0)
      {
       LOG_PRINT("\nReceived Out of sequence packet with sequence num %d,",seq_no);
       LOG_PRINT("\nLast received sequence num was :%d",call_info[call_indx].last_recvd_seq_num);
       var.num_of_out_of_seq_pkts++;
      }
     }
    else
    {
    if(seq_no != call_info[call_indx].last_recvd_seq_num + 1)
    {

      LOG_PRINT("\nReceived Out of sequence packet with sequence num %d,",seq_no);
      LOG_PRINT("\nLast received sequence num was :%d",call_info[call_indx].last_recvd_seq_num);
      var.num_of_out_of_seq_pkts++;
    }

    }
   }

    else if(ft_type == PACKET_TYPE_RTP)
    {
     
     if((call_info[call_indx].last_recvd_seq_num + 1) >= 0xFFFF)
     {
      if(seq_no != 0)
      {
       LOG_PRINT("\nReceived Out of sequence packet with sequence num %d,",seq_no);
       LOG_PRINT("\nLast received sequence num was :%d",call_info[call_indx].last_recvd_seq_num);
       var.num_of_out_of_seq_pkts++;
      }
     }

     else
     { 
      if(seq_no != call_info[call_indx].last_recvd_seq_num + 1)
      {
      LOG_PRINT("\nReceived Out of sequence packet with sequence num %d,",seq_no);
      LOG_PRINT("\nLast received sequence num was :%d",call_info[call_indx].last_recvd_seq_num);
      var.num_of_out_of_seq_pkts++;
     }    
    }
   }
   
    call_info[call_indx].last_recvd_seq_num = seq_no;
  }

  return;
}

void validate_packet_contents(S32 call_indx, U8 *buffer, S32 len, S32 ft_type, U16 seq_no)
{  
  U16 pkt_indx = 0, indx = 0;
  U8 packet_found = FT_FALSE, validation_needed = FT_FALSE;

  for(indx=0;indx<MAX_RTP_PKT_PER_CALL/2;indx++)
  {
    pkt_indx = call_info[call_indx].expected_packet_ref[indx];

    if(('\0' != pkt_indx) && ('\0' == packet_info[pkt_indx].packet_type))
    {
      break;
    }

    if(0 != packet_info[pkt_indx].expected_packet_length)
    {
      validation_needed = FT_TRUE;

      if((PACKET_TYPE_RTPC == ft_type))
      {
        if((len == (packet_info[pkt_indx].expected_packet_length + RTPC_HEADER_LENGTH)) && 
          (0 == memcmp((buffer+RTPC_HEADER_LENGTH), packet_info[pkt_indx].expected_pkt, packet_info[pkt_indx].expected_packet_length)))
        {
          packet_found = FT_TRUE;
          break;
        }
      }    
      else if((PACKET_TYPE_RTP == ft_type))
      {
        //  (RTP_HEADER_LENGTH(0)) is being used assuming that cc is always set to 0
        if((len == (packet_info[pkt_indx].expected_packet_length + (RTP_HEADER_LENGTH(0)))) && 
          (0 == memcmp((buffer+(RTP_HEADER_LENGTH(0))), packet_info[pkt_indx].expected_pkt, packet_info[pkt_indx].expected_packet_length)))
        {
          packet_found = FT_TRUE;
          break;
        }
      }
    }
  }

  if((FT_FALSE == packet_found) && (FT_TRUE == validation_needed))
  {
     LOG_PRINT("\nPacket received with sequence no. %d has corrupted content",seq_no);
    
    LOG_PRINT("\n\n-------------------- Corrupted payload --------------------");
    if((PACKET_TYPE_RTPC == ft_type))
    {
      U8 *pbuffer = buffer + RTPC_HEADER_LENGTH;
      hexdump_payload(&pbuffer,len-RTPC_HEADER_LENGTH);
      LOG_PRINT("\n-------------------------------------------------------------\n");
    }
    else
    {
      U8 *pbuffer = buffer + RTP_HEADER_LENGTH(0);
      hexdump_payload(&pbuffer,(len-(RTP_HEADER_LENGTH(0))));
      LOG_PRINT("\n-------------------------------------------------------------\n");
    }
    var.num_of_corrupt_pkts++;
  }

  return;
}

void send_ping_message(S32 ft_type)
{
  S8 command[100];
  if(PACKET_TYPE_RTP == ft_type)
  {
    sprintf(command, "%s %s", "ping -c 1", var.sbc_address);
  }
  system(command);
  return;
}


void fill_payload(U8* pdata, S8 *str,U16 *len)
{
    S8 *temp;
  S32 val;
    U16 ret_NL,ret_CR,ret_CRNL;  //ret values for strcmp to compare for new line and carriage return 
    temp = strtok(str," ");   
    while(temp !=NULL)
    {
     ret_NL = strcmp(temp,"\n") ; 
     ret_CR = strcmp(temp,"\r"); 
     ret_CRNL = strcmp(temp,"\r\n"); 
   
     if((ret_NL!=0) && (ret_CR!=0) && (ret_CRNL !=0))
     {
      sscanf(temp,"%x",&val);
      *pdata = val;
      pdata++;
     *len = *len + 1;
       if(len == MAX_PACKET_SIZE)
       {
         printf("packet size reached MAX_PAXKET_SIZE");
         return;
       }
     }
     temp = strtok(NULL," ");
    }

}


U8 send_pkt_single_group(U16 call_index)
{
	S32 length = 0,indx =0;
	U16 packet_index = 0;
	U8 error_flag = EXIT_SUCCESS;
	U8 hscsd_indx;

	if(call_info[call_index].is_valid == FT_TRUE)
	{
		/*curr_pkt_indx is used to keep track
		  of the pkt indx sent in the previous cycle
		*/

		indx = call_info[call_index].packet_grp[0].curr_pkt_indx;

		if(call_info[call_index].call_config.sbc_port != '\0')
		{
			/*If challenger is used for call configuration, 
			  the loop will work for 4 iterations
			*/
			if(0 == var.start_immediate_data)
			{
				//call_info[call_index].call_config.hscsd_no_of_port = 4;
			}
			if(('\0' == call_info[call_index].packet_grp[0].packet_ref[indx].packet_no)|| (call_info[call_index].packet_grp[0].curr_pkt_indx == MAX_RTP_PKT_PER_CALL/2))
			{
				call_info[call_index].packet_grp[0].curr_pkt_indx = 0;
				indx = call_info[call_index].packet_grp[0].curr_pkt_indx;
			}


			if('\0' != call_info[call_index].packet_grp[0].packet_ref[indx].packet_no)
			{
				packet_index = call_info[call_index].packet_grp[0].packet_ref[indx].packet_no;
				if((call_info[call_index].packet_grp[0].packet_ref[indx].skip == 0) || (call_info[call_index].packet_grp[0].packet_ref[indx].skip_after_cycle > 0))
				{
					for(hscsd_indx=0;hscsd_indx < call_info[call_index].call_config.hscsd_no_of_port;hscsd_indx++)
					{
						if((PACKET_TYPE_RTPC == packet_info[packet_index].packet_type) && (call_info[call_index].call_config.pater_ft_fd[hscsd_indx]) != '\0')
						{
							length = RTPC_HEADER_LENGTH + packet_info[packet_index].pkt_hdr.rtpc_hdr.length;
							LOG_PRINT("\nsending packet no:%d for call_id:%d:on port:%d\n",call_info[call_index].packet_grp[0].packet_ref[indx].packet_no,call_index+var.base_call_index,call_info[call_index].call_config.pater_ft_port[hscsd_indx]);
							error_flag = send_rtpc_packet(length, call_index, hscsd_indx,packet_index);

						}
					}
					call_info[call_index].packet_grp[0].packet_ref[indx].skip_after_cycle--;
					if(MAX_RTP_PKT_PER_CALL/2 > call_info[call_index].packet_grp[0].curr_pkt_indx)
					{
						call_info[call_index].packet_grp[0].curr_pkt_indx++;
					}

				}
				else if(call_info[call_index].packet_grp[0].packet_ref[indx].skip_after_cycle == 0)
				{
					LOG_PRINT("skipping packet id:%d \n",packet_index);

					/*Seq no. will be incremented even if the packet is skipped*/
					call_info[call_index].packet_grp[0].curr_pkt_indx++;
					call_info[call_index].packet_grp[0].packet_ref[indx].skip--;
				}

			}/*End of for(hscsd_ctr...*/

			/*update the seq_no and the TS after the packets on
			all the ports of the hscsd call has been sent*/

			call_info[call_index].rtp_seq_no++;
			call_info[call_index].timestamp =  call_info[call_index].timestamp + var.ts_delay;



		}/*End of if(call_info...etpc_port !=0 */
	}
	return error_flag;
}




U8 send_pkt_multi_group(U16 call_index)
{
        U16 packet_index = 0;
        S32 length = 0,indx =0;
        S32 chanel_num = 0;
        U8 error_flag = EXIT_SUCCESS;
        U8 hscsd_chanl;   /*used in case of HSCSD call to send more
                                         than 1 pkt on different ports for the same call in
                                         single cycle*/

        if(call_info[call_index].is_valid == FT_TRUE)
        {
              if(0 == var.start_immediate_data)
                        {
                         //       call_info[call_index].call_config.hscsd_no_of_port = 4;
                        }

           for(hscsd_chanl=0;hscsd_chanl < call_info[call_index].call_config.hscsd_no_of_port;hscsd_chanl++)
           {
               /*curr_pkt_indx is used to keep track
                *of the pkt indx sent in the previous cycle
                */

                indx = call_info[call_index].packet_grp[hscsd_chanl].curr_pkt_indx;

                if(call_info[call_index].call_config.sbc_port != '\0')
                {
                        if(('\0' == call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].packet_no)|| (call_info[call_index].packet_grp[hscsd_chanl].curr_pkt_indx == MAX_RTP_PKT_PER_CALL/2))
                        {
                                call_info[call_index].packet_grp[hscsd_chanl].curr_pkt_indx = 0;
                                indx = call_info[call_index].packet_grp[hscsd_chanl].curr_pkt_indx;
                        }

                        if('\0' != call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].packet_no)
                        {
                                packet_index = call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].packet_no;
                                if((call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].skip == 0) || (call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].skip_after_cycle > 0))
                                { 
                                                if((PACKET_TYPE_RTPC == packet_info[packet_index].packet_type) && (call_info[call_index].call_config.pater_ft_fd[hscsd_chanl]) != '\0')
                                                {
                                                        length = RTPC_HEADER_LENGTH + packet_info[packet_index].pkt_hdr.rtpc_hdr.length;
                                                        LOG_PRINT("\nsending packet no:%d for call_id:%d:on port:%d\n",call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].packet_no,call_index+var.base_call_index,call_info[call_index].call_config.pater_ft_port[hscsd_chanl]);
                                                        error_flag = send_rtpc_packet(length, call_index,hscsd_chanl,packet_index);

                                                }

                                        call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].skip_after_cycle--;
                                        if(MAX_RTP_PKT_PER_CALL/2 > call_info[call_index].packet_grp[hscsd_chanl].curr_pkt_indx)
                                        {
                                                call_info[call_index].packet_grp[hscsd_chanl].curr_pkt_indx++;
                                        }

                                }
                              else if(call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].skip_after_cycle == 0)
                              {
                                        LOG_PRINT("skipping packet id:%d \n",packet_index);

                                        /*Seq no. will be incremented even if the packet is skipped*/
                                        call_info[call_index].packet_grp[hscsd_chanl].curr_pkt_indx++;
                                        call_info[call_index].packet_grp[hscsd_chanl].packet_ref[indx].skip--;
                              }
                      }/* End of if('\0'!=call_info[call_index]...packet_no)*/          

                }/*End of if(call_info...etpc_port !=0 */
            }/*End of for(hscsd_ctr...*/

    
                        /*update the seq_no and the TS after the packets on
                        all the ports of the hscsd call has been sent*/

                        call_info[call_index].rtp_seq_no++;
                        call_info[call_index].timestamp =  call_info[call_index].timestamp + var.ts_delay;

}/*End of if(call_info[call_index].is_valid == FT_TRUE)*/
 
  return error_flag;
}/*End of send_pkt_multi_group*/ 



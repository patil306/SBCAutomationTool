#include "framethrower.ext"

S32 read_rtpc(FILE *fp, S8 *str, S32 packet_indx_start, S32 packet_indx_end)
{
  U32 i = 0, indx = 0, temp_variable = 0, expcted_pkt_indx = 0,index =0;
  S32 length = 0;
  U8 *pstart=NULL, *pdata=NULL, *ptemp=NULL;
  U16 param_val;  //value of the parameter
  U16 save_len = 0,ret_len = 0;
  do
  {
    if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
      linenumber++;
    if(check_string(str))
      continue;

    /*Read the information and save in the first packet in the range at index (packet_indx_start)
    Later, this information is copied to all the packets in the range.*/
    if(strstr(str,"SKIP"))
    {
      sscanf(str,"%s %hu",token,&packet_info[packet_indx_start].skip);
      continue;
    }

    if(strstr(str,"AFTER_CYCLES"))
    {
      sscanf(str,"%s %d",token,&packet_info[packet_indx_start].skip_after_cycle);
      continue;
    }

    if(strstr(str,"LENGTH"))
    {
      sscanf(str,"%s %hu",token,&(packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.length));      
      continue;
    }/* End of if(strstr(str,"LENGTH")*/

    if(strstr(str,"M_BIT"))
    {
      sscanf(str,"%s %hu",token,&param_val);
      packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.m_bit = param_val;
      continue;
    }/*End of if(strstr(str,"M_BIT")*/

    if(strstr(str,"PAYLOAD_TYPE"))
    {
      sscanf(str,"%s %hu",token,&param_val);
      packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.payload = param_val;

      if((0 < packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.length) && (MAX_PACKET_SIZE >= packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.length))        
      {
        for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
        {
          save_len = 0;
          memset(packet_info[indx].byte, 0, sizeof(MAX_PACKET_SIZE));
          pstart = packet_info[indx].byte;
          length = packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.length;
          pdata = pstart + RTPC_HEADER_LENGTH;
          i = 0;
          while(length > 0) 
          {
            /*Read the next line in the config file */
            if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
              linenumber++;

            /*If a blank line is encountred, this means the payload for the next pkt 
            starts. Thus stop parsing for the current packet.*/
            if(check_string(str))
            {
              break;
            }

            /* If PACKET_END is encountered,copy the header information in all the packets present in the range 
            from the first packet in the range and stop parsing for the payload */
            else if(strstr(str,"PACKET_END"))
            {
              for(index = packet_indx_start+1; index <= packet_indx_end; index++)
              {
                packet_info[index].skip = packet_info[packet_indx_start].skip;
                packet_info[index].skip_after_cycle = packet_info[packet_indx_start].skip_after_cycle;
                packet_info[index].pkt_hdr.rtpc_hdr.length = packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.length;
                packet_info[index].pkt_hdr.rtpc_hdr.m_bit = packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.m_bit;
                packet_info[index].pkt_hdr.rtpc_hdr.payload = packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.payload;
                packet_info[index].expected_packet_length = packet_info[packet_indx_start].expected_packet_length;

              }/*End of for(indx = packet_indx_start+1;...*/
              break;
            }
            /*If EXPECT_PKT_LEN is encountered then stop parsing for the payload and 
            start reading the expected payload */
            else if(strstr(str,"EXPECTED_PKT_LEN"))
            {
              sscanf(str,"%s %hu",token,&(packet_info[packet_indx_start].expected_packet_length));

              if((0 < packet_info[packet_indx_start].expected_packet_length) && (MAX_PACKET_SIZE >= packet_info[packet_indx_start].expected_packet_length))
              {
                for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
                {
                  i = 0;
                  for(expcted_pkt_indx = 0; expcted_pkt_indx < packet_info[packet_indx_start].expected_packet_length; expcted_pkt_indx++)
                  {
                    fscanf(fp,"%x",&temp_variable);
                    packet_info[indx].expected_pkt[expcted_pkt_indx] = temp_variable;
                    if(++i%8 == 0)
                    {
                      linenumber++;
                    }
                  }
                }/*End of if(packet_info[packet_indx_start]...*/
                if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
                  linenumber++;
              }/*End of for(expcted_pkt_indx = 0;...*/
              else if(0 == packet_info[packet_indx_start].expected_packet_length)
              {
                LOG_PRINT("Expected Payload length is 0 for packet_%u \n", packet_indx_start);
              }
              else
              {
                printf("Expected Payload length is not within the range 0 to %u for packet_%u \n", MAX_PACKET_SIZE, packet_indx_start);
                exit(0);
              }

            }
            else 
            {
              ret_len = 0;
              fill_payload(pdata + (save_len),str,&ret_len);
              save_len = save_len + ret_len;
              length = length - ret_len;
              if(length <= 0)
              {
                if(packet_indx_start != packet_indx_end)
                {
                  if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
                    linenumber++;
                  while(!(check_string(str)))
                  {
                    if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
                      linenumber++;
                  }
                }
                else
                {
                  continue;
                }
              }
            }
          }
          /*If the PACKET_END was encountered, break from the for loop also */
          if(strstr(str,"PACKET_END"))
          {
            break;
          }

        }/*End of for(indx = packet_indx_start; indx <= packet_indx_end...)*/

        if(strstr(str,"PACKET_END"))
        {
          break;
        }
      }
      else if(0 == packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.length)
      {
        LOG_PRINT("Payload length is 0 for packet_%u \n", packet_indx_start);
      }
      else
      {
        printf("Payload length is not within the range 0 to %u for packet_%u \n", MAX_PACKET_SIZE, packet_indx_start);
        exit(0);
      }
    }/*End of if(strstr(str,"PAYLOAD_TYPE")*/
    else if(strstr(str,"EXPECTED_PKT_LEN"))
    {
      sscanf(str,"%s %hu",token,&(packet_info[packet_indx_start].expected_packet_length));

      if((0 < packet_info[packet_indx_start].expected_packet_length) && (MAX_PACKET_SIZE >= packet_info[packet_indx_start].expected_packet_length))
      {
        for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
        {
          i = 0;
          for(expcted_pkt_indx = 0; expcted_pkt_indx < packet_info[packet_indx_start].expected_packet_length; expcted_pkt_indx++)
          {
            fscanf(fp,"%x", &temp_variable);          
            packet_info[indx].expected_pkt[expcted_pkt_indx] = temp_variable;
            if(++i%8 == 0)
            {
              linenumber++;
            }
          }
        }/*End of if(packet_info[packet_indx_start]...*/
        if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
          linenumber++;
      }/*End of for(expcted_pkt_indx = 0;...*/
      else if(0 == packet_info[packet_indx_start].expected_packet_length)
      {
        LOG_PRINT("Expected Payload length is 0 for packet_%u \n", packet_indx_start);
      }
      else
      {
        printf("Expected Payload length is not within the range 0 to %u for packet_%u \n", MAX_PACKET_SIZE, packet_indx_start);
        exit(0);
      }
      continue;
    }/* End of if(strstr(str,"EXPECTED_PKT_LEN")*/
    else if(strstr(str,"PACKET_END"))
    {
      /*Copy the header information in all the packets present in the range 
      from the first packet in the range*/

      for(indx = packet_indx_start+1; indx <= packet_indx_end; indx++)
      {
        packet_info[indx].skip = packet_info[packet_indx_start].skip;
        packet_info[indx].skip_after_cycle = packet_info[packet_indx_start].skip_after_cycle;
        packet_info[indx].pkt_hdr.rtpc_hdr.length = packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.length;
        packet_info[indx].pkt_hdr.rtpc_hdr.m_bit = packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.m_bit;
        packet_info[indx].pkt_hdr.rtpc_hdr.payload = packet_info[packet_indx_start].pkt_hdr.rtpc_hdr.payload;
        packet_info[indx].expected_packet_length = packet_info[packet_indx_start].expected_packet_length;

      }/*End of for(indx = packet_indx_start+1;...*/
      break;
    }
  }while(!feof(fp));  /*End of do-while */      


  /* Encode the RTPC packet by adding the header at the start of the payload */
  for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
  {
    pstart = packet_info[indx].byte;

    FT_ENCODE_RTPC_HEADER(pstart,
      ptemp, 
      packet_info[indx].pkt_hdr.rtpc_hdr.seq_no,
      packet_info[indx].pkt_hdr.rtpc_hdr.ts,
      packet_info[indx].pkt_hdr.rtpc_hdr.m_bit,
      packet_info[indx].pkt_hdr.rtpc_hdr.payload);
  }

  return 0;
}


/****************************************************************
*
*          FUNCTION : read_rtp()
*
****************************************************************/
S32 read_rtp(FILE *fp, S8 *str, S32 packet_indx_start, S32 packet_indx_end)
{
  U32 i = 0, index=0, cc = 0, indx = 0, temp_variable = 0, expcted_pkt_indx=0;
  S32 length = 0;
  U32 enc_index = 0;
  U8 *pstart=NULL, *pdata=NULL, *ptemp=NULL;
  U16 param_val;
  U16 save_len = 0,ret_len = 0;
  do
  {
    if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
      linenumber++;
    if(check_string(str))
      continue;

    if(strstr(str,"SKIP"))
    {
      sscanf(str,"%s %hu",token,&packet_info[packet_indx_start].skip);
      continue;
    }

    if(strstr(str,"AFTER_CYCLES"))
    {
      sscanf(str,"%s %d",token,&packet_info[packet_indx_start].skip_after_cycle);
      continue;
    }

    if(strstr(str,"LENGTH"))
    {
      sscanf(str,"%s %hu",token,&(packet_info[packet_indx_start].pkt_hdr.rtp_hdr.length));      
      continue;
    }/* End of if(strstr(str,"LENGTH")*/

    if(strstr(str,"VERSION"))
    {
      sscanf(str,"%s %hu",token,&param_val);
      packet_info[packet_indx_start].pkt_hdr.rtp_hdr.version = param_val;      
      continue;
    }

    if(strstr(str,"PADDING"))
    {
      sscanf(str,"%s %hu",token,&param_val);
      packet_info[packet_indx_start].pkt_hdr.rtp_hdr.padding = param_val;
      continue;
    }

    if(strstr(str,"X_BIT"))
    {
      sscanf(str,"%s %hu",token,&param_val);
      packet_info[packet_indx_start].pkt_hdr.rtp_hdr.x_bit = param_val;
      continue;
    }

    if(strstr(str,"CSRC"))
    {
      sscanf(str,"%s %hu",token,&param_val);
      packet_info[packet_indx_start].pkt_hdr.rtp_hdr.cc = param_val;
      continue;
    }

    if(strstr(str,"M_BIT"))
    {
      sscanf(str,"%s %hu",token,&param_val);
      packet_info[packet_indx_start].pkt_hdr.rtp_hdr.m_bit = param_val;
      continue;      
    }/*End of if(strstr(str,"M_BIT")*/

    if(strstr(str,"SSRC"))
    {
      sscanf(str,"%s %u",token,&packet_info[packet_indx_start].pkt_hdr.rtp_hdr.ssrc);
      continue;      
    }/*End of if(strstr(str,"SSRC")*/

    if(strstr(str,"CSRC") && (packet_info[packet_indx_start].pkt_hdr.rtp_hdr.cc))
    {
      sscanf(str,"%s ",token);
      while(cc < packet_info[packet_indx_start].pkt_hdr.rtp_hdr.cc)
      {
        fscanf(fp,"%hu",&packet_info[packet_indx_start].pkt_hdr.rtp_hdr.csrc[cc]);
        cc++;
        if(++i%4 == 0)
        {
          linenumber++;
        }
      }
    }/*End of if(strstr(str,CSRC)*/

    if(strstr(str,"PAYLOAD_TYPE"))
    {
      sscanf(str,"%s %hu",token,&param_val);
      packet_info[packet_indx_start].pkt_hdr.rtp_hdr.payload = param_val;

      if((0 < packet_info[packet_indx_start].pkt_hdr.rtp_hdr.length) && (MAX_PACKET_SIZE >= packet_info[packet_indx_start].pkt_hdr.rtp_hdr.length))
      {
        for(indx = packet_indx_start; indx <= packet_indx_end; indx++)      
        {
          save_len = 0;
          memset(packet_info[indx].byte, 0, sizeof(MAX_PACKET_SIZE));
          pstart = packet_info[indx].byte;
          length = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.length;
          pdata = pstart + (RTP_HEADER_LENGTH(packet_info[packet_indx_start].pkt_hdr.rtp_hdr.cc));
          while(length > 0) 
          {
            if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
              linenumber++;
            /*If a blank line is encountred, this means the payload for the next pkt 
            starts. Thus stop parsing for the current packet.*/
            if(check_string(str)) 
            {
              break;
            }
            /* If PACKET_END is encountered,copy the header information in all the packets present in the range 
            from the first packet in the range and stop parsing for the payload */
            else if(strstr(str,"PACKET_END"))
            { 
              for(index = packet_indx_start+1; index <= packet_indx_end; index++)
              {
                packet_info[index].skip = packet_info[packet_indx_start].skip;
                packet_info[index].skip_after_cycle = packet_info[packet_indx_start].skip_after_cycle;
                packet_info[index].pkt_hdr.rtp_hdr.length = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.length;
                packet_info[index].pkt_hdr.rtp_hdr.version = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.version;
                packet_info[index].pkt_hdr.rtp_hdr.padding = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.padding;
                packet_info[index].pkt_hdr.rtp_hdr.x_bit = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.x_bit;
                packet_info[index].pkt_hdr.rtp_hdr.cc = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.cc;
                packet_info[index].pkt_hdr.rtp_hdr.m_bit = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.m_bit;
                packet_info[index].pkt_hdr.rtp_hdr.ssrc = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.ssrc;
                for(cc=0; cc<packet_info[packet_indx_start].pkt_hdr.rtp_hdr.cc; cc++ )
                {
                  packet_info[index].pkt_hdr.rtp_hdr.csrc[cc] = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.csrc[cc];
                }
                packet_info[index].pkt_hdr.rtp_hdr.payload = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.payload;
                packet_info[index].expected_packet_length = packet_info[packet_indx_start].expected_packet_length;
              }/*End of for(indx = packet_indx_start+1;...*/

              break;
            }

            /*If EXPECT_PKT_LEN is encountered then stop parsing for the payload and 
            start reading the expected payload */
            else if(strstr(str,"EXPECTED_PKT_LEN"))
            {
              sscanf(str,"%s %hu",token,&(packet_info[packet_indx_start].expected_packet_length));

              if((0 < packet_info[packet_indx_start].expected_packet_length) && (MAX_PACKET_SIZE >= packet_info[packet_indx_start].expected_packet_length))
              {
                for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
                {
                  i = 0;
                  for(expcted_pkt_indx = 0; expcted_pkt_indx < packet_info[packet_indx_start].expected_packet_length; expcted_pkt_indx++)
                  {
                    fscanf(fp,"%x",&temp_variable);
                    packet_info[indx].expected_pkt[expcted_pkt_indx] = temp_variable;
                    if(++i%8 == 0)
                    {
                      linenumber++;
                    }
                  }
                }/*End of if(packet_info[packet_indx_start]...*/
                if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
                  linenumber++;
              }/*End of for(expcted_pkt_indx = 0;...*/
              else if(0 == packet_info[packet_indx_start].expected_packet_length)
              {
                LOG_PRINT("Expected Payload length is 0 for packet_%u \n", packet_indx_start);
              }
              else
              {
                printf("Expected Payload length is not within the range 0 to %u for packet_%u \n", MAX_PACKET_SIZE, packet_indx_start);
                exit(0);
              }
            }

            else
            {
              ret_len = 0;
              fill_payload(pdata + (save_len),str,&ret_len);
              save_len = save_len + ret_len;
              length = length - ret_len;
              if(length <= 0)
              {
                if(packet_indx_start != packet_indx_end)
                {
                  if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
                    linenumber++;
                  while(!(check_string(str)))
                  {
                    if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
                      linenumber++;
                  }
                }
                else
                {
                  continue;
                }
              }
            }
          }
          /*If the PACKET_END was encountered, break from the for loop also */
          if(strstr(str,"PACKET_END"))
          {
            break;
          }

        }/*End of for(indx = packet_indx_start; indx <= packet_indx_end...)*/
        if(strstr(str,"PACKET_END"))
        {
          break;
        }
      }/*End of if(packet_info[indx].pkt_hdr.rtp_hdr.length > 0 .....)*/       
      else if(0 == packet_info[packet_indx_start].pkt_hdr.rtp_hdr.length)
      {
        LOG_PRINT("Payload length is 0 for packet_%u \n", packet_indx_start);
      }
      else
      {
        printf("Payload length is not within the range 0 to %u for packet_%u \n", MAX_PACKET_SIZE, packet_indx_start);
        exit(0);
      }
    }/*End of if(strstr(str,"PAYLOAD_TYPE")*/
    else if(strstr(str,"EXPECTED_PKT_LEN"))
    {
      sscanf(str,"%s %hu",token,&(packet_info[packet_indx_start].expected_packet_length));

      if((0 < packet_info[packet_indx_start].expected_packet_length) && (MAX_PACKET_SIZE >= packet_info[packet_indx_start].expected_packet_length))
      {
        for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
        {
          i = 0;
          for(expcted_pkt_indx = 0; expcted_pkt_indx < packet_info[packet_indx_start].expected_packet_length; expcted_pkt_indx++)
          {
            fscanf(fp,"%x", &temp_variable);
            packet_info[indx].expected_pkt[expcted_pkt_indx] = temp_variable;
            if(++i%8 == 0)
            {
              linenumber++;
            }
          }
          if(fgets(str,MAX_LINE_SIZE,fp)!=NULL)
            linenumber++;
        }/*End of for indx = 0;*/
      }/*End of if(packet_info[packet_no].expected_packet_length > 0)*/
      else if(0 == packet_info[packet_indx_start].expected_packet_length)
      {
        LOG_PRINT("Expected payload length is 0 for packet_%u \n", packet_indx_start);
      }
      else
      {
        printf("Expected Payload length is not within the range 0 to %u for packet_%u \n", MAX_PACKET_SIZE, packet_indx_start);
        exit(0);
      }
      continue;
    }/* End of if(strstr(str,"EXPECTED_PKT_LEN")*/
    else if(strstr(str,"PACKET_END"))
    {
      /*Save the header information in all the packets present in the range*/
      for(indx = packet_indx_start+1; indx <= packet_indx_end; indx++)
      {
        packet_info[indx].skip = packet_info[packet_indx_start].skip;
        packet_info[indx].skip_after_cycle = packet_info[packet_indx_start].skip_after_cycle;
        packet_info[indx].pkt_hdr.rtp_hdr.length = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.length;
        packet_info[indx].pkt_hdr.rtp_hdr.version = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.version;
        packet_info[indx].pkt_hdr.rtp_hdr.padding = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.padding;
        packet_info[indx].pkt_hdr.rtp_hdr.x_bit = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.x_bit;
        packet_info[indx].pkt_hdr.rtp_hdr.cc = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.cc;
        packet_info[indx].pkt_hdr.rtp_hdr.m_bit = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.m_bit;
        packet_info[indx].pkt_hdr.rtp_hdr.ssrc = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.ssrc;
        for(cc=0; cc<packet_info[packet_indx_start].pkt_hdr.rtp_hdr.cc; cc++ )
        {
          packet_info[indx].pkt_hdr.rtp_hdr.csrc[cc] = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.csrc[cc];
        }
        packet_info[indx].pkt_hdr.rtp_hdr.payload = packet_info[packet_indx_start].pkt_hdr.rtp_hdr.payload;
        packet_info[indx].expected_packet_length = packet_info[packet_indx_start].expected_packet_length;
      }/*End of for(indx = packet_indx_start+1;...*/

      break;
    }
  }while(!feof(fp));  /*End of do-while */      


  /* Encode the RTP packet by adding the header at the start of the payload */

  for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
  {
    pstart = packet_info[indx].byte;

    FT_ENCODE_RTP_HEADER(pstart,
      ptemp,
      (packet_info[indx].pkt_hdr.rtp_hdr.version),
      (packet_info[indx].pkt_hdr.rtp_hdr.padding),
      (packet_info[indx].pkt_hdr.rtp_hdr.x_bit),
      (packet_info[indx].pkt_hdr.rtp_hdr.cc),
      (packet_info[indx].pkt_hdr.rtp_hdr.m_bit),
      (packet_info[indx].pkt_hdr.rtp_hdr.payload),
      (packet_info[indx].pkt_hdr.rtp_hdr.seq_no),
      (packet_info[indx].pkt_hdr.rtp_hdr.ts), 
      (packet_info[indx].pkt_hdr.rtp_hdr.ssrc),
      (packet_info[indx].pkt_hdr.rtp_hdr.csrc),
      enc_index); 

  }
  return 0;
}/*End of function rtp_read*/

/*********************************************************************
*
*   Function      :   read_config
*   Description   :   This function reads the configuration file and
*                     stores the information in the static variables  
*
**********************************************************************/


void read_config(FILE *fp)
{
  S32 call_no = -1;
  S32 packet_no = -1;
  S8 str[MAX_LINE_SIZE];
  S8 *call_temp,*substr,*temp,*pkt_temp;
  S8 equal;
  S32 call_indx,indx;
  S32 get_range_info = 0;   /*parses the range info from the config file only once*/
  S32 packet_indx_start = 0,packet_indx_end = 0;
	S32 pkt_no = 0;
  U16 port_var = 0;
  U16 port_loop = 0;

  do
  {
    fgets(str,MAX_LINE_SIZE,fp);
    linenumber++;
    if(check_string(str))
      continue;
#if 0
    if(strstr(str,"ETPC_PATER_ADDRESS") != NULL)
    {
      sscanf(str," %s %c %s",token,&equal,var.etpc_pater_address);
      LOG_PRINT(" %s : %s \n",token,var.etpc_pater_address);
      continue;
    }
#endif

    if(strstr(str,"SBC_ADDRESS") != NULL)
    {
      sscanf(str," %s %c %s",token,&equal,var.sbc_address);
      LOG_PRINT(" %s : %s \n",token,var.sbc_address);
      continue;
    }

    if(strstr(str,"FT_ADDRESS") != NULL)
    {
      sscanf(str,"%s %c %s",token,&equal,var.ft_address);
      LOG_PRINT(" %s : %s \n",token,var.ft_address);
      continue;
    }
#if 0
    if(strstr(str,"PATER_FT_ADDRESS") != NULL)
    {
      sscanf(str,"%s %c %s",token,&equal,var.pater_ft_address);
      LOG_PRINT(" %s : %s \n",token,var.pater_ft_address);
      continue;
    }
    if(strstr(str,"START_ERROR_PACKET") != NULL)
    {
      sscanf(str,"%s %c %u",token,&equal,&var.start_err_pkt);
      LOG_PRINT(" %s : %u \n",token,var.start_err_pkt);
      continue;
    }

    if(strstr(str,"END_ERROR_PACKET") != NULL)
    {
      sscanf(str,"%s %c %u",token,&equal,&var.end_err_pkt);
      LOG_PRINT(" %s : %u \n",token,var.end_err_pkt);
      continue;
    }

#endif
    if(strstr(str,"SET_DELAY") != NULL)
    {
      sscanf(str,"%s %c %u",token,&equal,&var.set_delay);
      LOG_PRINT(" %s : %u \n",token,var.set_delay);
      continue;
    }

    if(strstr(str,"TIMESTAMP_DELAY") != NULL)
    {
      sscanf(str,"%s %c %u",token,&equal,&var.ts_delay);
      LOG_PRINT(" %s : %u \n",token,var.ts_delay);
      continue;
    }

    if(strstr(str,"BASE_INDEX") != NULL)
    {
      sscanf(str,"%s %c %hu", token, &equal, &var.base_call_index);
      LOG_PRINT(" %s : %hu \n", token, var.base_call_index);
      continue;
    }

    if(strstr(str,"CALL_") != NULL)
    {
                        /*This flag must be set to zero each time 
                          a new call info is read from the cfg file */
                        get_range_info = 0;
      call_temp = strtok(str,"_");

      substr = strtok(NULL,"\0");

      /* && is used to provide range information.
      for e.g CALL_2&&6 means the information that follows in the config file till END_CALL is encounterd 
      applies to all calls ranging from call_2 to call_6 */

      if((strstr(substr,"&&") != NULL))
      {
#if 0
        call_temp = strtok(substr,"&&");
        call_no = atoi(call_temp);
        if(!(call_no >= 0 && call_no < MAX_NUM_CALLS))
        {
          printf("\n index for CALL_%d at linenumber:%d is invalid \n Valid range is CALL_0 - CALL_%d \n", call_no, linenumber, (MAX_NUM_CALLS - 1));
          exit(0);
        }

        call_indx = call_no; 
        while(call_temp !=NULL)
        {
          sscanf(call_temp,"%s %c %u",token,&equal,&call_no);
//          call_info[call_no].call_config.etpc_port = ETPC_FIRST_CALL_PORT + ((call_no + var.base_call_index) *2);

          call_temp = strtok(NULL,"&&"); //temp now contains the final packet_id
          if(call_temp != NULL)         
          {
            call_no = atoi(call_temp);
            if(!(call_no >= 0 && call_no < MAX_NUM_CALLS))
            {
              printf("\ncall_id for CALL_%d at linenumber:%d is Invalid \nValid range is CALL_0 - CALL_%d \n",call_no,linenumber,(MAX_NUM_CALLS - 1));
              exit(0);
            }
            if(!get_range_info)  /* parse the call info from config file only once for the range */
            {
              get_call_info(fp,call_indx);  
              if(var.start_immediate_data == 1) 
              {
                for(port_loop = 1; port_loop < call_info[call_indx].call_config.hscsd_no_of_port ;port_loop++)
                {
                  call_info[call_indx].call_config.pater_ft_port[port_loop] = call_info[call_indx].call_config.pater_ft_port[port_loop -1] +2;
                }
              }
              get_range_info = 1;
            }

            for(call_indx = call_indx + 1; call_indx <= call_no ; call_indx++)
            {
              /*In case call range is provided in the config file, the specified port is used 
              as the port for the first call in the range and the ports for all other calls in the range
              are calculated by incrementing the port of the previous call by 2 */
              port_var = call_info[call_indx -1].call_config.hscsd_no_of_port;
              call_info[call_indx].call_config.hscsd_no_of_port = port_var;
                                                        call_info[call_indx].call_config.packet_group = call_info[call_indx - 1].call_config.packet_group;
              call_info[call_indx].call_config.pater_ft_port[0] = ((call_info[call_indx - 1].call_config.pater_ft_port[port_var -1]) + 2); 
              for(port_loop = 1; port_loop < port_var ;port_loop++)
              {
                call_info[call_indx].call_config.pater_ft_port[port_loop] = call_info[call_indx].call_config.pater_ft_port[port_loop -1] +2;
              }
              call_info[call_indx].call_config.aoip_ft_port = ((call_info[call_indx - 1].call_config.aoip_ft_port) + 2);

              call_info[call_indx].call_config.etpc_port = ETPC_FIRST_CALL_PORT + ((call_indx + var.base_call_index) *2);
                                                        call_info[call_indx].timestamp = call_info[call_indx - 1].timestamp;
                                                        call_info[call_indx].init_seq_num = call_info[call_indx - 1].init_seq_num;
						        call_info[call_indx].rtp_seq_no = call_info[call_indx].init_seq_num;

              /*Packet_ref for all the calls in the range will be same*/

              for(indx=0; indx<MAX_RTP_PKT_PER_CALL; indx++)
              {
								for(pkt_no=0; pkt_no<HSCSD_NUM_OF_PORTS; pkt_no++)
								{
									if(0 == call_info[call_indx - 1].packet_grp[pkt_no].packet_ref[indx].packet_no)
                  break;
									call_info[call_indx].packet_grp[pkt_no].packet_ref[indx].packet_no = call_info[call_indx - 1].packet_grp[pkt_no].packet_ref[indx].packet_no; 
								}
              }
            }/*End for(call_indx..*/          
          }/*End of if(((call_temp != NULL) && (strstr(call_temp,"&&")*/
        }/*End of while(call_temp!=NULL)*/
#endif
      }/*End of if(strstr(substr,"&&")*/ 

      else   /*Single call configuration*/
      {
        call_no = atoi(substr);
        if(!(call_no >= 0 && call_no < MAX_NUM_CALLS))
        {
          printf("\ncall_id for CALL_%d at linenumber:%d is Invalid \nValid range is CALL_0 - CALL_%d \n",call_no,linenumber,(MAX_NUM_CALLS - 1));
          exit(0);
        }
        /*Read all information about the call*/ 
        get_call_info(fp,call_no); 
        if(var.start_immediate_data ==1)
        { 
          for(port_loop = 1; port_loop < call_info[call_no].call_config.hscsd_no_of_port ;port_loop++)
          {
            call_info[call_no].call_config.pater_ft_port[port_loop] = call_info[call_no].call_config.pater_ft_port[port_loop -1] +2;
          }
        }
        continue;
      }
    }/*End of if strstr(str,CALL_)*/

    if(strstr(str,"PACKET_") != NULL)
    {
      pkt_temp = strtok(str,"_");
      substr = strtok(NULL,"\0");

      if((strstr(substr,"@@") != NULL))
      {
        temp = strtok(substr,"@@");
        packet_indx_start = atoi(temp);
        packet_indx_end = packet_indx_start;    //intiialization to starting value

        /* Check that the packet num does not exceed the limit for MAX packets stored in packet_t */
        if(!(packet_indx_start > 0 && packet_indx_start < MAX_RTP_PACKETS))
        {
          printf("\npacket_no for PACKET_%d is Invalid \nValid range is PACKET_1 - PACKET_%u \n",packet_indx_start,(MAX_RTP_PACKETS - 1));
          exit(0);
        }

        while(temp !=NULL)
        {
          temp = strtok(NULL,"@@"); //temp now contains the final packet_id
          if(temp != NULL)         
          {
            packet_indx_end = atoi(temp);
            if(!(packet_indx_end > 0 && packet_indx_end < MAX_RTP_PACKETS))
            {
              printf("\npacket_no for PACKET_%d is Invalid \nValid range is PACKET_1 - PACKET_%u \n",packet_indx_end,(MAX_RTP_PACKETS - 1));
              exit(0);
            }
          }/*End of if(temp != NULL) */
        }/*End of while(temp !=NULL)*/

        get_packet_info(fp,packet_indx_start,packet_indx_end);
      }

      else
      {
        packet_no = atoi(substr);   //temp contains the packet_no
        if(!(packet_no > 0 && packet_no < MAX_RTP_PACKETS))
        {
          printf("\npacket_no for PACKET_%d is Invalid \nValid range is PACKET_1 - PACKET_%u \n",packet_no,(MAX_RTP_PACKETS - 1));
          exit(0);
        }


        get_packet_info(fp,packet_no,packet_no);
      }
      continue;
    }/*End of if(strstr(str,"PACKET_") */ 

  }while(!feof(fp)); /*End of do-while*/ 

  return;
}

/*********************************************************************
*
*   Function      :   get_call_info
*   Description   :   This function reads call information till END_CALL 
*                     is encountered in the config file and
*                     stores the info in the static variables.  
*
**********************************************************************/
void get_call_info(FILE *fp, S32 call_no)
{
  S8 str[MAX_LINE_SIZE];  
  S8 equal;
        U16 pkt_gp_indx=0;
  S32 pkt_no = -1;
  S32 pkt_indx = 0;  //index of the array for storing references of the packets to be sent
	S8 *temp,*substr;

  do
  {
    fgets(str,MAX_LINE_SIZE,fp);
    if(check_string(str))
    {
      linenumber++;
      continue;
    }
    linenumber++;

    if(strstr(str,"SBC_PORT") != NULL)
    {
      sscanf(str,"%s %c %hu",token,&equal,&call_info[call_no].call_config.sbc_port);
      LOG_PRINT("%s[%u] : %hu\n",token,call_no,call_info[call_no].call_config.sbc_port);
    }
    else if(strstr(str,"FT_PORT") != NULL)
    {
      sscanf(str,"%s %c %hu",token,&equal,&call_info[call_no].call_config.ft_port);
      LOG_PRINT("%s[%u] : %hu\n", token, call_no, call_info[call_no].call_config.ft_port);
    }
    else if((strstr(str,"HSCSD_NO_OF_PORT") != NULL))
    {
        sscanf(str,"%s %c %hu",token,&equal,&call_info[call_no].call_config.hscsd_no_of_port);
        LOG_PRINT("%s[%u] : %hu\n", token, call_no, call_info[call_no].call_config.hscsd_no_of_port);
      
    }/*End of if(strstr(str,"HSCSD_NO_OF_PORT")*/
		else if((strstr(str,"PACKET_GROUP") != NULL))
		{
			sscanf(str,"%s %c %hu",token,&equal,&call_info[call_no].call_config.packet_group);
			LOG_PRINT("%s[%u] : %hu\n", token, call_no, call_info[call_no].call_config.packet_group);

		}/*End of if(strstr(str,"PACKET_GROUP")*/

		else if(strstr(str,"PACKET_REF_") != NULL)
    {
                       pkt_indx = 0;
                       substr = strtok(str,"_");
                       substr = strtok(NULL,"_");
                       substr = strtok(NULL,"=");
                       /*PACKET_REF_1 will be internally stored at array index 0. 
                         thus the value is decremented by 1*/
                       pkt_gp_indx = (atoi(substr) - 1);
                       substr = strtok(NULL,"\0");

			if((strstr(substr,"&&") != NULL))
      {
				temp = strtok(substr,"&&");

                        pkt_no = atoi(temp);					
        /* Check that the packet num does not exceed the limit for MAX packets stored in packet_t */
        if(!((pkt_no) >= 1 && (pkt_no) < MAX_RTP_PACKETS))
        {
          LOG_PRINT("\npacket no %d in PACKET_REF for CALL_%d is Invalid \nValid range is 1 - %u \n",pkt_no,call_no,(MAX_RTP_PACKETS - 1));
          exit(0);
        }

				call_info[call_no].packet_grp[pkt_gp_indx].packet_ref[pkt_indx].packet_no = pkt_no;
        while(temp !=NULL)
        {
          temp = strtok(NULL,"&&"); //temp now contains the final packet_id
          if(temp != NULL)         
          {
            pkt_no = atoi(temp);
            if(!(pkt_no >= 1 && pkt_no < MAX_RTP_PACKETS))
            {
              LOG_PRINT("\npacket no %d in PACKET_REF for CALL_%d is Invalid \nValid range is 1 - %u \n",pkt_no,call_no,(MAX_RTP_PACKETS));
              exit(0);
            } 

						for(pkt_indx=pkt_indx+1; call_info[call_no].packet_grp[pkt_gp_indx].packet_ref[pkt_indx-1].packet_no != pkt_no; pkt_indx++)
            {
              if(pkt_indx > MAX_RTP_PKT_PER_CALL - 1)
              {
                LOG_PRINT("\nPACKET_REF for CALL_%d specifies more packets than %u ",call_no, MAX_RTP_PKT_PER_CALL);
                break;
              }
							call_info[call_no].packet_grp[pkt_gp_indx].packet_ref[pkt_indx].packet_no = call_info[call_no].packet_grp[pkt_gp_indx].packet_ref[pkt_indx - 1].packet_no + 1;
            }
          }/*End of if(temp != NULL)*/
        }
      }/*End of if(strstr(str,"&&")*/ 
      else 
      {
				temp = strtok(substr,"&");
        while(temp !=NULL)
        {
					
                                        pkt_no = atoi(temp);					
          if(!((pkt_no) >= 1 && (pkt_no) < MAX_RTP_PACKETS))
          {
            LOG_PRINT("\npacket no %d in PACKET_REF for CALL_%d is Invalid \nValid range is 1 - %u \n",pkt_no,call_no,(MAX_RTP_PACKETS - 1));
            exit(0);
          }
          if(pkt_indx > (MAX_RTP_PKT_PER_CALL -1))
          {
            LOG_PRINT("\nPACKET_REF for CALL_%d specifies more packets than %u ",call_no, MAX_RTP_PKT_PER_CALL);
            break;
          }
					call_info[call_no].packet_grp[pkt_gp_indx].packet_ref[pkt_indx].packet_no = pkt_no;
          pkt_indx++;
          temp = strtok(NULL,"&"); //temp now contains the packet_id
          if(temp != NULL) 
          {
            pkt_no = atoi(temp);
            if(!(pkt_no >= 1 && pkt_no < MAX_RTP_PACKETS))
            {
              LOG_PRINT("\npacket no %d in PACKET_REF for CALL_%d is Invalid \nValid range is 1 - %u \n",pkt_no,call_no,(MAX_RTP_PACKETS - 1));
              exit(0);
            }
          }
        }
      }
    }/*End of if(strstr(str,"PACKET_REF")*/
    else if(strstr(str,"SEQ_NUM"))
    {
      sscanf(str,"%s %c %u",token,&equal,&call_info[call_no].init_seq_num);
      call_info[call_no].rtp_seq_no = call_info[call_no].init_seq_num;
      continue;
    }/*End of if(strstr(str,"SEQ_NUM") */
    else if(strstr(str,"TIMESTAMP"))
    {
      sscanf(str,"%s %c %u",token,&equal,&call_info[call_no].timestamp);
      continue;
    }/*End of if(strstr(str,"SEQ_NUM") */
    else if(strstr(str,"END_CALL"))
    {
      break; 
    }
    else
    {
      LOG_PRINT("\nINFO: Line %d: is not a call config Parameter\n",linenumber); 
    }
  }while(!feof(fp));        
}/*End of function get_call_info */

/*********************************************************************
*
*   Function      :   get_packet_info
*   Description   :   This function reads packet information till PACKET_END 
*                     is encountered in the config file and
*                     stores the info in the static variables.  
*
**********************************************************************/
void get_packet_info(FILE *fp, S32 packet_indx_start, S32 packet_indx_end)
{
  S32 indx = 0;
  S8 str[MAX_LINE_SIZE];

  do
  {
    fgets(str,MAX_LINE_SIZE,fp);
    if(check_string(str))
    {                
      linenumber++;
      continue;
    }
    linenumber++;

    if(strstr(str,"PACKET_TYPE RTPC"))
    {
      if(packet_indx_start != packet_indx_end)
      {
        LOG_PRINT("Packet type for Packets %u - %u is RTPC \n", packet_indx_start, packet_indx_end);
      }
      else
      {
        LOG_PRINT("Packet type for Packet %u is RTPC \n", packet_indx_start);
      }

      for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
      {
        if(MAX_RTP_PACKETS > indx)
        {
          packet_info[indx].packet_type = PACKET_TYPE_RTPC;
        }
        else
        {
          printf(" No. of packets exceeded %u",MAX_RTP_PACKETS - 1);
          exit(0);
        }
      }/*End of for(indx = packet_indx_start;...*/
      read_rtpc(fp,str,packet_indx_start,packet_indx_end);

    }/*End of if(strstr(str,"PACKET_TYPE RTPC"))*/

    else if(strstr(str,"PACKET_TYPE RTP")) 
    {
      if(packet_indx_start != packet_indx_end)
      {
        LOG_PRINT("Packet type for Packets %u  - %u is RTP \n", packet_indx_start, packet_indx_end);
      }
      else
      {
        LOG_PRINT("Packet type for Packet %u is RTP \n", packet_indx_start);
      }
      for(indx = packet_indx_start; indx <= packet_indx_end; indx++)
      {
        if(MAX_RTP_PACKETS > indx)
        {
          packet_info[indx].packet_type = PACKET_TYPE_RTP;
        }
        else
        {
          printf(" No of packets exceeded %u \n",MAX_RTP_PACKETS - 1);
          exit(0);
        }
      }/*End of for(indx = packet_indx_start;...*/

      read_rtp(fp,str,packet_indx_start,packet_indx_end);
    }
    else
    {
      printf(" First parameter after PACKET_[%u] shall be PACKET_TYPE \n", packet_indx_start);
    }

    if(strstr(str,"PACKET_END"))
    {
      break;
    }
  }while(!feof(fp));  /*End of do-while */  

  return;    
}/*End of funcion get_packet_info*/





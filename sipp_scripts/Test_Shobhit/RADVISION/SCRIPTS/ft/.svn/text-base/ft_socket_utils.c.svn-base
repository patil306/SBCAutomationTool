#include "framethrower.ext"

/****************************************************************
*
*          FUNCTION : send_rtp_packet
*
****************************************************************/

U8 send_rtp_packet(S32 length , S32 call_index, S32 packet_no)
{
  S32 len = 0;

  /*Fill and update the timestamp of the packet for this call*/ 
  packet_info[packet_no].pkt_hdr.rtp_hdr.ts =  call_info[call_index].timestamp;
  call_info[call_index].timestamp =  call_info[call_index].timestamp + var.ts_delay;

  /* if the seq_no. stored in the call_info is not 0, 
  *  this means it has been incremented after the first cycle. 
  *  Use this updated value of the seq_no.
  */

  if(call_info[call_index].rtp_seq_no != 0 )
  {
    packet_info[packet_no].pkt_hdr.rtp_hdr.seq_no = call_info[call_index].rtp_seq_no;
    LOG_PRINT("RTP seq no =%d",packet_info[packet_no].pkt_hdr.rtp_hdr.seq_no);
  }

  //update the Seq_no & TS in the payload also
  packet_info[packet_no].byte[2] = (packet_info[packet_no].pkt_hdr.rtp_hdr.seq_no >> 8) & 0xFF;
  packet_info[packet_no].byte[3] = (packet_info[packet_no].pkt_hdr.rtp_hdr.seq_no) & 0xFF;
  packet_info[packet_no].byte[4] = (packet_info[packet_no].pkt_hdr.rtp_hdr.ts >> 24) & 0xFF;
  packet_info[packet_no].byte[5] = (packet_info[packet_no].pkt_hdr.rtp_hdr.ts >> 16) & 0xFF;
  packet_info[packet_no].byte[6] = (packet_info[packet_no].pkt_hdr.rtp_hdr.ts >> 8)  & 0xFF;
  packet_info[packet_no].byte[7] = (packet_info[packet_no].pkt_hdr.rtp_hdr.ts & 0xFF);

  if((len = sendto(call_info[call_index].call_config.aoip_ft_fd,
    packet_info[packet_no].byte,
    length,
    0,
    (struct sockaddr *)&call_info[call_index].call_config.etpc_addr,
    sizeof(call_info[call_index].call_config.etpc_addr))) == -1)
  {
    LOG_PRINT("send_rtp_packet error in sendto");
    return 1;
  }

  else
  {
    var.num_of_pkts_sent++;
    LOG_PRINT(" No of Bytes Sent : %d \n",len);
    LOG_PRINT("\n =====================");
    LOG_PRINT("\n SENT RTP PACKET \n");
    LOG_PRINT(" =====================\n");
    print_rtp_packet(packet_info[packet_no].byte, len);
  }

  return 0;
} /* function send_rtp_packet ends */

/****************************************************************
*
*          FUNCTION : send_rtpc_packet
*
****************************************************************/

U8 send_rtpc_packet(S32 length , S32 call_index, U8 hscsd_index,S32 packet_no)
{
  S32 len = 0;
  /*Fill the timestamp of the packet for this call*/ 
  packet_info[packet_no].pkt_hdr.rtpc_hdr.ts =  call_info[call_index].timestamp;


  /* if the seq_no. stored in the call_info is not 0,
  *  this means it has been incremented after the first cycle.
  *  Use this updated value of the seq_no.
  */

  if(call_info[call_index].rtp_seq_no != 0 )
  {
    packet_info[packet_no].pkt_hdr.rtpc_hdr.seq_no = call_info[call_index].rtp_seq_no;
  }

  //update the Seq_no & TS in the payload also
  packet_info[packet_no].byte[0] = (packet_info[packet_no].pkt_hdr.rtpc_hdr.seq_no & 0xFF);
  packet_info[packet_no].byte[1] = (packet_info[packet_no].pkt_hdr.rtpc_hdr.ts >> 8)  & 0xFF;
  packet_info[packet_no].byte[2] = (packet_info[packet_no].pkt_hdr.rtpc_hdr.ts & 0xFF);

  if((len = sendto(call_info[call_index].call_config.pater_ft_fd[hscsd_index],
    packet_info[packet_no].byte,
    length,
    0,
    (struct sockaddr *)&call_info[call_index].call_config.etpc_addr,
    sizeof(call_info[call_index].call_config.etpc_addr))) == -1)
  {
    LOG_PRINT("send_rtpc_packet error in sendto");
    return 1;
  }

  else
  {
    var.num_of_pkts_sent++;
		LOG_PRINT("RTP Seq no = %d",packet_info[packet_no].pkt_hdr.rtpc_hdr.seq_no);
    LOG_PRINT(" No of Bytes Sent : %d \n",len);
    LOG_PRINT("\n =====================");
    LOG_PRINT("\n SENT RTPC PACKET \n");
    LOG_PRINT(" =====================\n");
    print_rtpc_packet(packet_info[packet_no].byte,len);
  }

  return 0;
} /* function send_rtpc_packet ends */


/****************************************************************
*
*          FUNCTION : open_pater_ft_ports()
*
****************************************************************/
void open_pater_ft_ports()
{
  struct hostent *hp;
  S32 call_id = 0;
  U16 port_var = 0;
  U16 port_loop = 0;

  FD_ZERO(&var.rd_fdset);
  var.max_fd = -1;


  /*Open a port to receive challenger messages*/
  if((var.challenger_sock_id = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
  {
    printf("\n Socket call failed for challenger socket");
    exit(errno);
  }

  if (!(hp = gethostbyname ((S8 *)var.pater_ft_address)))
  {
    printf(" open_pater_ft_ports: Unknown server for PATER_FT_ADDRESS %s \n",var.pater_ft_address);
    exit(0);
  }

  memset((S8 *)&var.challenger_sock, 0, sizeof (var.challenger_sock));
  memcpy((S8 *)&var.challenger_sock.sin_addr, (S8 *) hp->h_addr, hp->h_length );

  var.challenger_sock.sin_family = AF_INET;
  var.challenger_sock.sin_port = htons(var.challenger_port);

  if(bind(var.challenger_sock_id, (struct sockaddr *)&var.challenger_sock,
    sizeof(var.challenger_sock)) < 0)
  {
    printf(" Bind failed for challenger_port:%d",var.challenger_port);
    printf(" (errno = %d) \n",errno);
    exit(errno);
  }
  fcntl(var.challenger_sock_id, F_SETFL, O_NONBLOCK);
  FD_SET(var.challenger_sock_id, &var.rd_fdset);

  FD_ZERO(&var.rd_fdset);
  /* set address and bind ports for all calls*/
  if(1 == var.start_immediate_data)
  {
    for(call_id = 0; call_id < MAX_NUM_CALLS; call_id++)
    {
      if(MAX_NUM_OF_PORTS == num_of_open_ports)
      {
				printf("\n\n Maximum number of ports : %d have been opened \n\n",num_of_open_ports);
        break;
      }
      if('\0' != call_info[call_id].call_config.sbc_port)
      {
        port_var = call_info[call_id].call_config.hscsd_no_of_port;
        for(port_loop = 0; port_loop < port_var; port_loop++)
        {
          if(MAX_NUM_OF_PORTS > num_of_open_ports)
          {
            if((call_info[call_id].call_config.pater_ft_fd[port_loop] = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
            {
              printf("\n Socket call failed for call_index = %u", call_id);
              exit(errno);
            }
            if (!(hp = gethostbyname ((S8 *)var.pater_ft_address)))
            {
              printf(" open_pater_ft_ports: Unknown server for PATER_FT_ADDRESS %s \n",var.pater_ft_address);
              exit(0);
            }
            memset((S8 *)&call_info[call_id].call_config.pater_ft_addr, 0, sizeof (call_info[call_id].call_config.pater_ft_addr));
            memcpy((S8 *)&call_info[call_id].call_config.pater_ft_addr.sin_addr, (S8 *) hp->h_addr, hp->h_length );
            call_info[call_id].call_config.pater_ft_addr.sin_family = AF_INET;
            call_info[call_id].call_config.pater_ft_addr.sin_port = htons(call_info[call_id].call_config.pater_ft_port[port_loop]);

            if(bind(call_info[call_id].call_config.pater_ft_fd[port_loop], (struct sockaddr *)&call_info[call_id].call_config.pater_ft_addr,
              sizeof(call_info[call_id].call_config.pater_ft_addr)) < 0)
            {
              LOG_PRINT(" Bind failed for PATER_FT_PORT = %d PATER_FT_IP:%s pater_ft_fd = %d for call_index %u ",call_info[call_id].call_config.pater_ft_port[port_loop], var.pater_ft_address, call_info[call_id].call_config.pater_ft_fd[port_loop],call_id);
              LOG_PRINT(" (errno = %d) \n",errno);
              exit(errno);
            }
            num_of_open_ports++;
            LOG_PRINT(" Socket opened and binded Succesfully for PATER_FT_PORT = %d pater_ft_fd = %d for call_index %u & IP %s \n",
              call_info[call_id].call_config.pater_ft_port[port_loop],
              call_info[call_id].call_config.pater_ft_fd[port_loop],
              call_id ,
              var.pater_ft_address);

          }/*End of if(MAX_NUM_OF_PORTS > num_of_open_ports)*/    

          else
          {
            printf("\n\n Maximum number of ports have opened = %d \n\n",num_of_open_ports);
            break;
          }

        }
        if(call_info[call_id].call_config.pater_ft_fd[port_loop] > var.max_fd)
          var.max_fd = call_info[call_id].call_config.pater_ft_fd[port_loop];

        /* Save ETPC address for each call */
        if((hp = gethostbyname(var.etpc_pater_address)) == NULL)
        {
          printf(" open_pater_ft_ports: Unknown server for ETPC_PATER_ADDRESS%s \n",var.etpc_pater_address);
          exit(0);
        }

       // LOG_PRINT(" ETPC_PATER_ADDRESS stored for CALL_ID %d ETPC_PORT %d & IP %s \n",call_id,call_info[call_id].call_config.etpc_port,var.etpc_pater_address);

        memcpy((S8 *)&call_info[call_id].call_config.etpc_addr.sin_addr,(S8 *)hp->h_addr,hp->h_length);
        call_info[call_id].call_config.etpc_addr.sin_family = hp->h_addrtype;
        call_info[call_id].call_config.etpc_addr.sin_port=htons(call_info[call_id].call_config.sbc_port);
      }
    }
  }
  //  for reception at ETPC side at PATER-FT
  {
    if((call_info[MAX_NUM_CALLS].call_config.pater_ft_fd[0] = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
    {
      printf("\n Socket call failed for ETPA at PATER FT \n");
      exit(errno);
    }
    if (!(hp = gethostbyname ((S8 *)var.pater_ft_address)))
    {
      printf(" open_pater_ft_ports: Unknown server for PATER_FT_ADDRESS %s \n",var.pater_ft_address);
      exit(0);
    }
    memset((S8 *)&call_info[MAX_NUM_CALLS].call_config.pater_ft_addr, 0, sizeof (call_info[MAX_NUM_CALLS].call_config.pater_ft_addr));
    memcpy((S8 *)&call_info[MAX_NUM_CALLS].call_config.pater_ft_addr.sin_addr, (S8 *) hp->h_addr, hp->h_length );
    call_info[MAX_NUM_CALLS].call_config.pater_ft_addr.sin_family = AF_INET;
    call_info[MAX_NUM_CALLS].call_config.pater_ft_addr.sin_port = htons(call_info[MAX_NUM_CALLS].call_config.pater_ft_port[0]);

    if(bind(call_info[MAX_NUM_CALLS].call_config.pater_ft_fd[0], (struct sockaddr *)&call_info[MAX_NUM_CALLS].call_config.pater_ft_addr,
      sizeof(call_info[MAX_NUM_CALLS].call_config.pater_ft_addr)) < 0)
    {
      LOG_PRINT(" Bind failed for PATER_FT_PORT = %d PATER_FT_IP:%s pater_ft_fd = %d for ETPA \n",call_info[MAX_NUM_CALLS].call_config.pater_ft_port, var.pater_ft_address[0], call_info[MAX_NUM_CALLS].call_config.pater_ft_fd[0]);
      LOG_PRINT(" (errno = %d) \n",errno);
      exit(errno);
    }
    LOG_PRINT("\n Socket opened and binded Succesfully for PATER_FT_PORT = %d pater_ft_fd = %d for ETPA & IP %s \n",
      call_info[MAX_NUM_CALLS].call_config.pater_ft_port[0],
      call_info[MAX_NUM_CALLS].call_config.pater_ft_fd[0],
      var.pater_ft_address);

  }

  var.max_fd++;
} /* Function open_pater_ft_ports() ends */

/****************************************************************
*
*          FUNCTION : open_aoip_ft_ports()
*
****************************************************************/

void open_aoip_ft_ports()
{  
  struct hostent *hp;
  S32 call_id = 0;

  FD_ZERO(&var.rd_fdset);
  var.max_fd = -1;


  /*Open a port to receive challenger messages*/
  if((var.challenger_sock_id = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
  {
    printf("\n Socket call failed for challenger socket");
    exit(errno);
  }

  if (!(hp = gethostbyname ((S8 *)var.ft_address)))      
  {
    printf(" open_aoip_ft_ports: Unknown server for AoIP_FT_ADDRESS %s \n",var.ft_address);
    exit(0);
  }

  memset((S8 *)&var.challenger_sock, 0, sizeof (var.challenger_sock));
  memcpy((S8 *)&var.challenger_sock.sin_addr, (S8 *) hp->h_addr, hp->h_length );

  var.challenger_sock.sin_family = AF_INET;
  var.challenger_sock.sin_port = htons(var.challenger_port);

  if(bind(var.challenger_sock_id, (struct sockaddr *)&var.challenger_sock,
    sizeof(var.challenger_sock)) < 0)
  {
    printf(" Bind failed for challenger_port:%d",var.challenger_port);
    printf(" (errno = %d) \n",errno);
    exit(errno);
  }

  if(1 == var.start_immediate_data)
  {
    /* set address and bind ports for all calls*/
    for(call_id = 0; call_id < MAX_NUM_CALLS; call_id++)
    {
      /*If the call has been configured through config. file, its etpc_port is set to 
      a non-zero value using its call_id. If the config. file doesnot have its entry,
      no packets are sent for this call,So no need to open a socket for this call */

      if('\0' != call_info[call_id].call_config.sbc_port)
      {
        if((call_info[call_id].call_config.aoip_ft_fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
        {
          printf("\n Socket call failed for call_index[%u] \n", call_id);
          exit(errno);
        }
        if (!(hp = gethostbyname ((S8 *)var.ft_address)))      
        {
          printf(" open_aoip_ft_ports: Unknown server for AoIP_FT_ADDRESS %s for call_index[%u] \n",var.ft_address, call_id);
          exit(0);
        }
        memset((S8 *)&call_info[call_id].call_config.aoip_ft_addr, 0, sizeof (call_info[call_id].call_config.aoip_ft_addr));
        memcpy((S8 *)&call_info[call_id].call_config.aoip_ft_addr.sin_addr, (S8 *) hp->h_addr, hp->h_length );

        call_info[call_id].call_config.aoip_ft_addr.sin_family = AF_INET;
        call_info[call_id].call_config.aoip_ft_addr.sin_port = htons(call_info[call_id].call_config.ft_port);

        if(bind(call_info[call_id].call_config.aoip_ft_fd, (struct sockaddr *)&call_info[call_id].call_config.aoip_ft_addr,
          sizeof(call_info[call_id].call_config.aoip_ft_addr)) < 0)
        {
          printf(" Bind failed for AoIP_FT_PORT = %d AoIP_FT_IP:%s aoip_ft_fd = %d for call_index %u ",call_info[call_id].call_config.ft_port, var.ft_address, call_info[call_id].call_config.aoip_ft_fd,call_id);
          printf(" (errno = %d) \n",errno);
          exit(errno);
        }
        LOG_PRINT(" Socket opened and binded Succesfully for AoIP_FT_PORT = %d aoip_ft_fd = %d for call_index %u & IP %s \n",
          call_info[call_id].call_config.ft_port,
          call_info[call_id].call_config.aoip_ft_fd,
          call_id ,
          var.ft_address);

        fcntl(call_info[call_id].call_config.aoip_ft_fd, F_SETFL, O_NONBLOCK);
        FD_SET(call_info[call_id].call_config.aoip_ft_fd, &var.rd_fdset);

        if(call_info[call_id].call_config.aoip_ft_fd > var.max_fd)
          var.max_fd = call_info[call_id].call_config.aoip_ft_fd;

        /* Save ETPC address for each call */
        if((hp = gethostbyname(var.sbc_address)) == NULL)
        {
          printf(" open_aoip_ft_ports: Unknown server for ETPC_AoIP_ADDRESS %s for call_index %u \n",var.sbc_address, call_id);
          exit(0);
        }

        LOG_PRINT(" ETPC_AoIP_ADDRESS stored for call_index %d ETPC_PORT %d & IP %s \n",call_id,call_info[call_id].call_config.sbc_port,var.sbc_address);

        memcpy((S8 *)&call_info[call_id].call_config.etpc_addr.sin_addr,(S8 *)hp->h_addr,hp->h_length);
        call_info[call_id].call_config.etpc_addr.sin_family = hp->h_addrtype;
        call_info[call_id].call_config.etpc_addr.sin_port=htons(call_info[call_id].call_config.sbc_port);
      }
    } /*End of for */
  }

  var.max_fd++;
} /* Function open_aoip_ft_ports() ends */

/*********************************************************************
*
*   Function      :   listen_challenger_port 
*   Description   :   This function listens to challenger port to receive 
*                     start and stop messages for calls
*   Return Value  :   Returns "error_flag".
*                       error_flag = 0 means no error
*                       error_flag = 1 means error
*
**********************************************************************/
void listen_challenger_port(U32 packet_type)
{
  U8 recv_buff[MAX_PACKET_SIZE];
  U16 call_index = 0xFF;
  U32 a_len = sizeof(struct sockaddr_in);
  S32 len = -1;
  U16 port_loop = 0; 
  U8 buff = 0; 
  struct sockaddr_in address;


  memset(recv_buff, '\0', sizeof(S8) * MAX_PACKET_SIZE);
  if ((len = recvfrom(var.challenger_sock_id, recv_buff,
    MAX_PACKET_SIZE, MSG_DONTWAIT, (struct sockaddr *)&address,&a_len)) > 0)
  {
		/*Extract the call id from recv_buff*/
    call_index = (*((U16 *)(recv_buff + 2)));
    LOG_PRINT("\n\ncall_index = %u, msg_type = %u \n", call_index, (*((U16 *)recv_buff)));

    call_index = call_index - var.base_call_index;

    if(MAX_NUM_CALLS -1 < call_index)
    {
      printf("\n Invalid call received from challenger with call index : %u",call_index);
      return;
    }

    /*First two bytes of the recv_buff give the msg_id*/
    if((*((U16 *)recv_buff)) == START_DATA)
    {
      /*If the data for the call is already started,ignore this message*/
      if (call_info[call_index].is_valid == FT_TRUE)
      {
        LOG_PRINT("\nSTART DATA received for call_id:%d,when the data is already started",call_index);
        //continue;   
      }
      call_info[call_index].is_valid = FT_TRUE;
    }
    else if((*((U16 *)recv_buff)) == STOP_DATA)
    {
      /*If the data for the call is already started,ignore this message*/
      if (call_info[call_index].is_valid == FT_FALSE)
      {
        LOG_PRINT("\nSTOP DATA received for call_id:%d,when the data is already stopped",call_index);
        //continue;   
      }
      else
      {
        /*Change the value for is_valid*/
        call_info[call_index].is_valid = FT_FALSE;
        if(PACKET_TYPE_RTPC == packet_type)
        {
          for(port_loop = 0; port_loop < HSCSD_NUM_OF_PORTS; port_loop++)
          {
            close(call_info[call_index].call_config.pater_ft_fd[port_loop]);
            call_info[call_index].call_config.pater_ft_fd[port_loop] = 0;
          }
        }
        else if(PACKET_TYPE_RTP == packet_type)
        {
          close(call_info[call_index].call_config.aoip_ft_fd);
          call_info[call_index].call_config.aoip_ft_fd = 0;
        }
      }
    }

    else if((*((U16 *)recv_buff)) == CONFIGURE_CALL)
    {

      if (call_info[call_index].is_valid == FT_TRUE)
      {
        LOG_PRINT("\n START DATA received for call_id:%d,when the data is already started",call_index);
      }
      else
      {
		for(port_loop = 0; port_loop < HSCSD_NUM_OF_PORTS; port_loop++)
        {
          call_info[call_index].call_config.pater_ft_port[port_loop] = (*((U16 *)(recv_buff + 4 + buff)));
          LOG_PRINT("\n Received port from challenger is %hu for call %d \n\n ",call_info[call_index].call_config.pater_ft_port[port_loop],call_index);
          buff = buff+2;

          /*All the invalid ports i.e ports less than 49152 are set to zero so that a socket is not opened for an invalid port */ 
          if(ETPC_FIRST_CALL_PORT > call_info[call_index].call_config.pater_ft_port[port_loop])
          {
            call_info[call_index].call_config.pater_ft_port[port_loop] = 0;
          }

          /*Increment the hscsd_no_of_port for all the ports which are non-zero */
        }
        if(PACKET_TYPE_RTPC == packet_type)
        {
          open_pater_ft_port_for_call(call_index);
        }
        call_info[call_index].call_config.ft_port = (*((U16 *)(recv_buff + 12)));
        if(PACKET_TYPE_RTP == packet_type)
        {
          open_aoip_ft_port_for_call(call_index);
        }
      }
    }

    else
    {
      LOG_PRINT("Invalid message received from challenger with msg_id : %d",(*((U16 *)recv_buff)));
    }
  }/*End of if(len=recvfrom..)*/
}/*End of function listen_challenger_port*/

void open_aoip_ft_port_for_call(S32 call_id)
{
  struct hostent *hp;

  /*If the call has been configured through config. file, its etpc_port is set to 
  a non-zero value using its call_id. If the config. file doesnot have its entry,
  no packets are sent for this call,So no need to open a socket for this call */

  if('\0' != call_info[call_id].call_config.sbc_port)
  {
    if(0 != call_info[call_id].call_config.aoip_ft_fd)
    {
      printf("\n Socket[%u] already opened for this call \n", call_info[call_id].call_config.aoip_ft_fd);
      return;
    }
    if((call_info[call_id].call_config.aoip_ft_fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
    {
      printf("\n Socket call failed for call_index = %u \n", call_id);
      return;
    }
    if (!(hp = gethostbyname ((S8 *)var.ft_address)))      
    {
      printf(" open_aoip_ft_port_for_call: Unknown server for AoIP_FT_ADDRESS %s \n",var.ft_address);
      return;
    }
    memset((S8 *)&call_info[call_id].call_config.aoip_ft_addr, 0, sizeof (call_info[call_id].call_config.aoip_ft_addr));
    memcpy((S8 *)&call_info[call_id].call_config.aoip_ft_addr.sin_addr, (S8 *) hp->h_addr, hp->h_length );

    call_info[call_id].call_config.aoip_ft_addr.sin_family = AF_INET;
    call_info[call_id].call_config.aoip_ft_addr.sin_port = htons(call_info[call_id].call_config.ft_port);

    if(bind(call_info[call_id].call_config.aoip_ft_fd, (struct sockaddr *)&call_info[call_id].call_config.aoip_ft_addr,
      sizeof(call_info[call_id].call_config.aoip_ft_addr)) < 0)
    {
      printf(" Bind failed for AoIP_FT_PORT = %d AoIP_FT_IP:%s aoip_ft_fd = %d for call_index %u ",call_info[call_id].call_config.ft_port, var.ft_address, call_info[call_id].call_config.aoip_ft_fd,call_id);
      printf(" (errno = %d) \n",errno);
      return;
    }
    LOG_PRINT(" Socket opened and binded Succesfully for AoIP_FT_PORT = %d aoip_ft_fd = %d for call_index %u & IP %s \n",
      call_info[call_id].call_config.ft_port,
      call_info[call_id].call_config.aoip_ft_fd,
      call_id ,
      var.ft_address);

    fcntl(call_info[call_id].call_config.aoip_ft_fd, F_SETFL, O_NONBLOCK);
    FD_SET(call_info[call_id].call_config.aoip_ft_fd, &var.rd_fdset);

    if(call_info[call_id].call_config.aoip_ft_fd > var.max_fd)
      var.max_fd = call_info[call_id].call_config.aoip_ft_fd;

    /* Save ETPC address for each call */
    if((hp = gethostbyname(var.sbc_address)) == NULL)
    {
      printf(" open_aoip_ft_port_for_call: Unknown server for ETPC_AoIP_ADDRESS%s \n",var.sbc_address);
      return;
    }

    LOG_PRINT(" ETPC_AoIP_ADDRESS stored for CALL_ID %d ETPC_PORT %d & IP %s \n",call_id,call_info[call_id].call_config.sbc_port,var.sbc_address);

    memcpy((S8 *)&call_info[call_id].call_config.etpc_addr.sin_addr,(S8 *)hp->h_addr,hp->h_length);
    call_info[call_id].call_config.etpc_addr.sin_family = hp->h_addrtype;
    call_info[call_id].call_config.etpc_addr.sin_port=htons(call_info[call_id].call_config.sbc_port);
  }
}

void open_pater_ft_port_for_call(S32 call_id)
{
  struct hostent *hp;
  U16 port_loop = 0;

  if('\0' != call_info[call_id].call_config.sbc_port)
  {
		LOG_PRINT("CALL INDEX IS %u",call_id);
    for(port_loop = 0; port_loop < HSCSD_NUM_OF_PORTS; port_loop++)
    {
      if(MAX_NUM_OF_PORTS > num_of_open_ports)
      {
        if(0 != call_info[call_id].call_config.pater_ft_fd[port_loop])
        {
					printf("\n Socket[%u] already opened for this call \n", call_info[call_id].call_config.pater_ft_fd);
          return;
        }

        /*Sockets are opened only for the ports with non zero value */ 
        if(0 != call_info[call_id].call_config.pater_ft_port[port_loop])
        { 
          if((call_info[call_id].call_config.pater_ft_fd[port_loop] = socket(AF_INET, SOCK_DGRAM, 0)) < 0)
          {
            printf("\n Socket call failed for call_index = %u", call_id);
            return;
          }

          if (!(hp = gethostbyname ((S8 *)var.pater_ft_address)))
          {
            printf(" open_pater_ft_port_for_call: Unknown server for PATER_FT_ADDRESS %s \n",var.pater_ft_address);
            return;
          }
          memset((S8 *)&call_info[call_id].call_config.pater_ft_addr, 0, sizeof (call_info[call_id].call_config.pater_ft_addr));
          memcpy((S8 *)&call_info[call_id].call_config.pater_ft_addr.sin_addr, (S8 *) hp->h_addr, hp->h_length );

          call_info[call_id].call_config.pater_ft_addr.sin_family = AF_INET;
          call_info[call_id].call_config.pater_ft_addr.sin_port = htons(call_info[call_id].call_config.pater_ft_port[port_loop]);

          if(bind(call_info[call_id].call_config.pater_ft_fd[port_loop], (struct sockaddr *)&call_info[call_id].call_config.pater_ft_addr,
            sizeof(call_info[call_id].call_config.pater_ft_addr)) < 0)
          {
            LOG_PRINT(" Bind failed for PATER_FT_PORT = %d PATER_FT_IP:%s pater_ft_fd = %d for call_index %u ",call_info[call_id].call_config.pater_ft_port[port_loop], var.pater_ft_address, call_info[call_id].call_config.pater_ft_fd[port_loop],call_id);
            LOG_PRINT(" (errno = %d) \n",errno);
            return;
          }
         num_of_open_ports++;
          LOG_PRINT(" Socket opened and binded Succesfully for PATER_FT_PORT = %d pater_ft_fd = %d for call_index %u & IP %s \n",
            call_info[call_id].call_config.pater_ft_port[port_loop],
            call_info[call_id].call_config.pater_ft_fd[port_loop],
            call_id ,
            var.pater_ft_address);
				}/*End of if(0 != call_info[call_id].call_config.pater_ft_port[port_loop])*/
      }/*End of if(MAX_NUM_OF_PORTS > num_of_open_ports)*/
      else
      {
        printf("\n\n Maximum number of ports have opened = %d \n\n",num_of_open_ports);
        break;
      }

      if(call_info[call_id].call_config.pater_ft_fd[port_loop] > var.max_fd)
        var.max_fd = call_info[call_id].call_config.pater_ft_fd[port_loop];
    }/* End of for (port_loop = 0; port_loop < port_var; port_loop++) */
    /* Save ETPC address for each call */
    if((hp = gethostbyname(var.etpc_pater_address)) == NULL)
    {
      printf(" open_pater_ft_port_for_call: Unknown server for ETPC_PATER_ADDRESS%s \n",var.etpc_pater_address);
      return;
    }

    LOG_PRINT(" ETPC_PATER_ADDRESS stored for CALL_ID %d ETPC_PORT %d & IP %s \n",call_id,call_info[call_id].call_config.sbc_port,var.etpc_pater_address);

    memcpy((S8 *)&call_info[call_id].call_config.etpc_addr.sin_addr,(S8 *)hp->h_addr,hp->h_length);
    call_info[call_id].call_config.etpc_addr.sin_family = hp->h_addrtype;
    call_info[call_id].call_config.etpc_addr.sin_port=htons(call_info[call_id].call_config.sbc_port);
  }
}






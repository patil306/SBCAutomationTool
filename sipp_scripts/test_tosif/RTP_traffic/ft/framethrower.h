#ifndef __FRAME_THROWER_H
#define __FRAME_THROWER_H

#include <stdio.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>
#include <string.h>
#include <stdarg.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include <netdb.h>
#include <pthread.h>


#define FT_TRUE 0
#define FT_FALSE 1 

#define CYCLE_INTERVAL  20  //time interval between two cycles is 20 ms 

/*Message received from challenger*/
#define START_DATA 1
#define STOP_DATA  2
#define CONFIGURE_CALL  3

#define PACKET_TYPE_RTPC 1
#define PACKET_TYPE_RTP 2

#define MAX_FILE_NAME 100
#define MAX_LINE_SIZE 65535
#define MAX_IP_STR_SIZE 16
#define MAX_CSRC_COUNT 15

/* Num of calls per FT is increased to 1000 
  and total num of calls for FT is increased to 5040 */
#define MAX_NUM_CALLS 1000
#define MAX_CALL_ID 5040

#define MAX_RTP_PACKETS 5001  // Packet index starts from 1-5000;zero is unused
#define MAX_PACKET_SIZE 1000  // 256   
#define MAX_RTP_PKT_PER_CALL 2000
#define MAX_NUM_OF_PORTS MAX_NUM_CALLS  
#define HSCSD_NUM_OF_PORTS 4

#define ETPA_RECEPTION_PORT 65534
#define ETPC_FIRST_CALL_PORT 49152

#define RTPC_HEADER_LENGTH 4
#define RTP_HEADER_LENGTH(c) (12+(c*4))

#define IPV4_HDR_LENGTH 20
#define UDP_HDR_LENGTH 8

/*Payload Types*/
#define G711_U_LAW 0
#define CSD_TRAU_FRAME 95
#define GSM_FR_CODEC 3
#define G711_A_LAW 8 
#define GSM_EFR_CODEC 110
#define GSM_HR_CODEC 111
#define AMR_FR_CODEC 112
#define AMR_HR_CODEC 112
#define AMR_WB_CODEC 113
#define CLEAR_MODE 120

typedef char S8;
typedef unsigned char U8;
typedef unsigned short int U16;
typedef int S32;
typedef unsigned int U32;
typedef unsigned long long U64;

S32 linenumber;  /* keeps track of the linenumber in the config file.
				   displayed while printing error messages */
U8 log_flag;
U16 num_of_open_ports;

#define LOG_PRINT if(log_flag)printf


/* Defines whether the packet group 
single or multi is used for the multi packet call.
*/
enum pkt_grp_t
{
	PKT_GRP_SINGLE,	/* value 0 means pkt_group single is used */
	PKT_GRP_MULTI		/* value 1 means pkt_group multi is used */
};


typedef struct
{
  U32 sbc_port;
  U16 pater_ft_port[4];
  U16 ft_port;
  S32 pater_ft_fd[4];
  S32 aoip_ft_fd;
  struct sockaddr_in etpc_addr;
  struct sockaddr_in pater_ft_addr;
  struct sockaddr_in aoip_ft_addr;
  U16 hscsd_no_of_port;
  enum pkt_grp_t packet_group;  /*For AoIP, this value will always remain 0(single) */      
}call_t;


typedef struct {
	S8 etpc_pater_address[MAX_IP_STR_SIZE];
  S8 sbc_address[MAX_IP_STR_SIZE];
	S8 ft_address[MAX_IP_STR_SIZE];
  S8 pater_ft_address[MAX_IP_STR_SIZE];	
	U64 num_of_pkts_sent;
	U64 num_of_pkts_recvd;
  U64 num_of_out_of_seq_pkts;
  U64 num_of_corrupt_pkts;
	U32 rtpc_ts[MAX_NUM_CALLS];
	U32 rtp_ts[MAX_NUM_CALLS];
	U32 set_delay;
	U32 ts_delay;
	fd_set rd_fdset;
	S32 max_fd;
  S32 challenger_sock_id;
  struct sockaddr_in challenger_sock;
  U32 challenger_port;
  U32 ctr_disp_interval;
  U32 num_of_cycles;
  U16 start_immediate_data;
  U16 base_call_index;
  S32 start_err_pkt;
  S32 end_err_pkt;
}variable_str;

typedef struct
{
  U16 length;
  U16 ts;
  U8 seq_no;
  U8 payload;
  U8 m_bit;
}rtpc_t;


typedef struct
{
  U32 ts;
  U32 ssrc;
  U16 length;
  U16 seq_no;
  U16 csrc[MAX_CSRC_COUNT];
  U8 version;
  U8 padding;
  U8 x_bit;
  U8 cc;
  U8 m_bit;
  U8 payload;
}rtp_t;

#define FT_ENCODE_RTPC_HEADER(pstart,\
                              p,\
                              seq_no,\
                              ts,\
                              m_bit,\
                              pt) \
p = pstart;\
*p = seq_no;\
p++;\
*p = (ts >> 8)&0xFF;\
p++;\
*p = ts & 0xFF;\
p++; \
*p = (m_bit&0x01)<<7;\
*p |= pt&0x7F;\
p++;

#define FT_ENCODE_RTP_HEADER(pstart,\
                             p,\
                             version,\
                             padding,\
                             x_bit,\
                             cc,\
                             m_bit,\
                             pt,\
                             seq_no,\
                             ts,\
                             ssrc,\
                             csrc,\
                             index) \
p = pstart;\
  *p = (version&0x03)<<6;\
*p |= (padding&0x01)<<5;\
*p |= (x_bit&0x01)<<5;\
*p |= (cc&0x0F);\
p++;\
*p = (m_bit&0x01)<<7;\
*p |= (pt&0x7F);\
p++;\
*p = (seq_no >> 8)&0xFF;\
p++;\
*p = (seq_no)&0xFF;\
p++;\
*p =  (ts >> 24)&0xFF;\
p++;\
*p =  (ts >> 16)&0xFF;\
p++;\
*p =  (ts >> 8)&0xFF;\
p++;\
*p =  (ts&0xFF);\
p++;\
*p =  (ssrc >> 24)&0xFF;\
p++;\
*p =  (ssrc >> 16)&0xFF;\
p++;\
*p =  (ssrc >> 8)&0xFF;\
p++;\
*p =  (ssrc&0xFF);\
p++;\
while(index != cc){\
*p =  (csrc[index] >> 24)&0xFF;\
p++;\
*p =  (csrc[index] >> 16)&0xFF;\
p++;\
*p =  (csrc[index] >> 8)&0xFF;\
p++;\
*p =  (csrc[index]&0xFF);\
p++;\
index++;\
}\
p++;


typedef union
{
  rtpc_t rtpc_hdr;
  rtp_t rtp_hdr;
}pkt_hdr_t;


typedef struct
{ 
  U32 packet_type;
  U16 skip;
  U32 skip_after_cycle;
  U16 expected_packet_length;  
  pkt_hdr_t pkt_hdr;  
  U8 byte[MAX_PACKET_SIZE];
  U8 expected_pkt[MAX_PACKET_SIZE];  
}packet_t;


/*This structure is used to save the references of packets for each calls alongwith their skip values*/

typedef struct
{
  U16 packet_no;
  U16 skip;
  U32 skip_after_cycle;
}packet_ref_t;


typedef struct
{ 
  packet_ref_t packet_ref[MAX_RTP_PKT_PER_CALL];
	U16 curr_pkt_indx;
}packet_grp_t;


typedef struct
{ 
  U16 expected_packet_ref[MAX_RTP_PKT_PER_CALL/2]; 
  U32 rtp_seq_no; //seq_no for each packet increments after the pkt is sent
  call_t call_config;
  packet_grp_t packet_grp[HSCSD_NUM_OF_PORTS];
  U8 is_valid; 
  U32 init_seq_num;  //seq no. of the first packet of the call
  U32 timestamp;  //seq no. of the first packet of the call
  U16 last_recvd_seq_num; //seq no.of the previous packet received for this call
}call_info_t;
#endif




#include<iostream>
#include <stdint.h>
using namespace std;

int main()
{
 typedef enum
 {
        SIP_SDP_OFFER_RCVD = 0x00000100,	///offer rcvd
	SIP_SDP_OFFER_SENT = 0x00000200		///offer sent
 }sip_sdp_direction_enum;

typedef enum
{ 
SIP_SDP_OFFER_NONE			= 0,						///NO offer outstanding
	SIP_SDP_OFFER_RCVD_INVITE	= 1 | SIP_SDP_OFFER_RCVD,	///offer received in INVITE
	SIP_SDP_OFFER_RCVD_18X		= 2 | SIP_SDP_OFFER_RCVD,	///offer received in 18x 100rel
	SIP_SDP_OFFER_RCVD_200		= 3 | SIP_SDP_OFFER_RCVD,	///offer received in 200
	SIP_SDP_OFFER_RCVD_PRACK	= 4 | SIP_SDP_OFFER_RCVD,	///offer received in PRACK
	SIP_SDP_OFFER_RCVD_UPDATE	= 5 | SIP_SDP_OFFER_RCVD,	///offer received in UPDATE
	SIP_SDP_OFFER_SENT_INVITE	= 6 | SIP_SDP_OFFER_SENT,
	SIP_SDP_OFFER_SENT_18X		= 7 | SIP_SDP_OFFER_SENT,
	SIP_SDP_OFFER_SENT_200		= 8 | SIP_SDP_OFFER_SENT,
	SIP_SDP_OFFER_SENT_PRACK	= 9 | SIP_SDP_OFFER_SENT,
	SIP_SDP_OFFER_SENT_UPDATE	=10 | SIP_SDP_OFFER_SENT,
} sip_sdp_state_enum;

typedef struct
{
    	sip_sdp_state_enum		sip_sdp_state;
} sip_b2b_invite_session_info_t; 

sip_b2b_invite_session_info_t   mSessionModification;

        mSessionModification.sip_sdp_state= SIP_SDP_OFFER_RCVD_INVITE ;
        cout<<mSessionModification . sip_sdp_state;
	//typedef unsigned __int32 uint32_t;
return 0;
}

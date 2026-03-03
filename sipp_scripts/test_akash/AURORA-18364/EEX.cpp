#include<iostream>
using namespace std;

int main()
{
int actions=0;
typedef enum
{
	MCE_ACTION_REMOTE_MCB 			= 1 << 0,
	MCE_ACTION_INTERSECT_MCB 		= 1 << 1,
	MCE_ACTION_AUGMENT_MCB 			= 1 << 2,
	MCE_ACTION_RESERVE_PORTS 		= 1 << 3,
	MCE_ACTION_ACQUIRE_NEW_PORTS 		= 1 << 4,
	MCE_ACTION_SECURE_MEDIA			= 1 << 5,
	MCE_ACTION_ANTI_TROMBONING		= 1 << 6,
	MCE_ACTION_MEDIA_RELINQUISH		= 1 << 7,
	MCE_ACTION_SIPREC	        	= 1 << 8,
	MCE_ACTION_ANAT_MCB                     = 1 << 9,
	MCE_ACTION_ANAT_REQUIRED		= 1 << 10,
	MCE_ACTION_CALL_RECONSTRUCTION  	= 1 << 11,
	MCE_ACTION_FULL_ANAT_OFFER		= 1 << 12
} MceActionTypeEnum;


cout<<actions |= MCE_ACTION_FULL_ANAT_OFFER;
return 0;
}

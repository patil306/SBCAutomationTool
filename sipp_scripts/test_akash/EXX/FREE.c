#include<stdio.h> 
#include<stdlib.h> 
int main() 
{ 
	char* rtcp_packet_after_update = NULL; 
//	int *ptr1 = &x; 
	int *ptr2 = (int *)malloc(sizeof(int)); 
//	int *ptr3 = new int; 
//	int *ptr4 = NULL; 

	/* delete Should NOT be used like below because x is allocated 
 * 		on stack frame */
    
    free(rtcp_packet_after_update);

return 0;
}

#include<iostream>
using namespace std;
int main()
{
//int a = 0x01234567; 
//char *p = &i;
    
    unsigned int i = 1;  
    char *c = (char*)&i;  
    if (*c) 
	{
		cout<<"value =" <<&i;
        	cout<<"\n"<<"Little endian \n "; 
	} 
    else
	{
		cout<<"value =" <<*c;
        	cout<<"Big endian";  
	}
    return 0;  
}   

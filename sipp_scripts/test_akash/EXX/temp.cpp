// C program to illustrate 
i// strcmp() function 

#include<iostream.h> 
#include<string>
using namespace std; 
int main() 
{ 
	// z has greater ASCII value than g 
	char leftStr[] = "+000108079110"; 
	char rightStr[] = "000108079110"; 
	
	int res = strcmp(leftStr, rightStr); 
	
	if (res==0) 
		cout<<"Strings are equal"; 
	else
		cout<<"Strings are unequal"; 
		
	cout<<"\nValue of result "<<res ;
	
	return 0; 
} 


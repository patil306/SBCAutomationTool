/*#include<iostream>
#include<string.h>
using namespace std;
*/
#include<stdio.h>
#include<string.h>

void concat(char *a,char *b)
{
   printf("\n  A =%s",a);
   printf("\n  B =%s",b);

   while(*a)
   {
      a=a+1;
        printf("\n CONCAT =%s",a);
   }

   while(*b)
   {
       *a++ = *b++;
       printf("\n WHILE =%s",b);
   }

   printf("\n CONCAT =%s",a);
  *a='\0';

   printf("\n CAT =%s",a);
}

/*
void concat(string a,string b)
{
 while(*a)
  a++;
 while(*b)
 *a++ = *b++;

*a='\0';
}*/


int main()
{
 //string a= "AKASH";
 //string b="SINGH";
//char a[]="AKASH";
//char b[]="SINGH"; 

 const char *a = "AKASH";
 const char *b ="SINGH";
  concat(a,b);
// printf("CONCAT =%s",d);
// cout<<"\n CONCAT ="<<concat(a,b);
 return 0;
}

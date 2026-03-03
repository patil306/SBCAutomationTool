#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

void swap(char *str1, char *str2)
{
  char *temp = str1;
  str1 = str2;
  str2 = temp;
}  

void Palindrome(const char *str)
{
int len = strlen(str);
int palin =1;
cout<<"\n LEN="<<len;
  for(int i=0; i<=len;i++)
  {
    if(str[i]==str[len-1])
    {
    len--;
    }
    else
    {
    cout<<"\n STRING is not palindrome";
    palin=0;
    break;
    }
  }
  if(palin==1)
  cout<<"\n STRING is palindrome";
}

void Reverse(const char *str)
{
  
  while(*str)
  {
   str++;
   Reverse(str);
  }
}
   
int main()
{
  const char *str1 = "SANNA";
  const char *str2 = "forgeeks";
  
 // Palindrome(str1);
  cout<<"\n RVERSE ="<<Reverse(str1);
  swap(str1, str2);
  cout<<"\n AKASH STR1= "<<str1<<"\n STR2 = "<<str2;

//  printf("str1 is %s, str2 is %s", str1, str2);
  getchar();
  return 0;
}

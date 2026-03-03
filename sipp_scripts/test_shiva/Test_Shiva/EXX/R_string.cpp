#include<iostream>
using namespace std;
int main()
{
 char a[10];
 int len;
 //cout<<"\n ENTER the STRING=";
 cout<<" ENTER LEN="<<endl;
 cin>>len;
 cout<<" ENTER the STRING="<<endl;
 for(int i=0;i<len;i++)
 {
 cin>>a[i];
 }
 for(int i=0;i<len;i++)
 {
 cout<<a[i];
 } 
 return 0;
}

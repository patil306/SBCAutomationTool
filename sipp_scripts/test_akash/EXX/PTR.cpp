#include<iostream>
//#include<stdio.h>
//#include<string.h>
using namespace std; 
class Akash
{
public:
//int static kane = 10;

};


int main() 
{
//string uri = "sbcdev4.com";
//int *mode_map= NULL;
//cout<<"Eneter = "<<uri.size();
//gets(uri);
Akash *a= NULL;

int b= 10;
a=(Akash*) &b;

if(a)
{
cout<<"Value ="<<a;
//delete a;
}
delete a;
return 0;
}

#include<iostream>
//#include <iomanip>
using namespace std;
struct A
{
int a;
};

int main()
{
int b=10232;
int *p = &b;
struct A *ptr = (struct A *) 20000;
cout<<"\n SIZE OF P ="<<sizeof(p);
cout<<"\n AT =" <<*p;
cout<<"\n SIZE OF ="<<sizeof(ptr);
cout<<"\n KANE ="<<(long)ptr;
cout<<"\n AA="<<long(ptr +3)<<"\n";
return 0;
}

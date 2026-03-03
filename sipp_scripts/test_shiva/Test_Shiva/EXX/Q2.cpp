#include<iostream>
using namespace std;
struct A
{
int a;
};

int main()
{
struct A *ptr = (struct A *) 20000;
cout<<ptr +3;
return 0;
}

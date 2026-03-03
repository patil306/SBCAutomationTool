#include<iostream>
#include<vector>
#include<utility>
#include<map>
using namespace std;
void fun(int *x);
main()
{
    int q=10;
   //int *q=&a;
 fun(&q); //line no 10
 cout<<q;
}
void  fun(int *x)
{
    int b=20;
    x = &b;
}

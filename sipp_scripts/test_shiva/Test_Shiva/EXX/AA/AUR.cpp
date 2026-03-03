#include <iostream>

using namespace std;
void fun (int *a);
int main()
{
   int *p=0;
   fun(p);
   {
       if(*p=1)
       cout <<"work";
       else
       cout<<"TT="<<*p;
   }
    return 0;
}

void fun(int *a)
{
     *a=1;
}

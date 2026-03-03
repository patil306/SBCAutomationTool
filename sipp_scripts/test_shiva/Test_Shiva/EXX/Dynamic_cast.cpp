#include<iostream>
using namespace std;

class Base
{
	virtual void akash()
	{
	cout<<"\n akash fun()";
	}
};

class Derived1 : public Base
{
	void derived_akash()
        {
        cout<<"\n derived_akash fun()";
        }
};

class Derived2 : public Base
{
        void derived_akash()
        {
        cout<<"\n derived_D2_akash fun()";
        }
};

int main()
{
     Derived1 d1;

     Base *bp=dynamic_cast<Base*>(&d1);
    
     Derived2 *dp2= dynamic_cast<Derived2*>(bp);
     if( dp2 == NULL)
	cout<<"NULL";
     return 0;
}

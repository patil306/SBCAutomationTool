#include<iostream>
using namespace std;

class SipB2b
{
public:
 virtual void print()
  { cout<<"SipB2b";}
};

class SipB2bInCo:public SipB2b
{
  void print()
  { cout<<"SipB2bInCo";}
};

class SipB2bInRe: public SipB2b
{
  void print()
  { cout<<"SipB2bInRe";}
};


int main()
{
SipB2b *mCurState;
SipB2b *state = dynamic_cast<SipB2b*> (mCurState);
state->print();
return 0;
}

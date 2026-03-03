#include<iostream>
#include<vector>
using namespace std;

int main()
{
vector<int> myvector;
cout<<"\n SIZE ="<<myvector.size();
myvector.resize(256);
cout<<"\n SIZE1 ="<<myvector.size();
	for(int i=1;i<=200;i++)
	{
	cout<<"\n before SIZE ="<<myvector.size();
		myvector.push_back(i);
	cout<<"\n after SIZE ="<<myvector.size();
	}
cout<<"\n SIZE2 ="<<myvector.size();
	for(int i=1;i<=100;i++)
		myvector.push_back(i+500);
cout<<"\n SIZE3 ="<<myvector.size();
return 0;
}

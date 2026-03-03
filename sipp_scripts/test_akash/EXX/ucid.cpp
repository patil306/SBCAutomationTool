#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
string lUserToUser = "P;DFE0000F"; 
string lUserToUser_old = "PDFE00F";
//lUserToUser.erase ( lUserToUser.begin(), lUserToUser.begin()+lUserToUser.find ("00F")+3);
cout <<" AKASH lUserToUser = "<<lUserToUser<<endl;
/*size_t loc = (lUserToUser.find (';'));
		cout<<" \n location="<<loc ;
			string templUserToUsr = "ASOFFFAD;";
               		string lucid; 
		        //size_t loc = (templUserToUsr.find (';'));
			int a;
                        if(loc != string::npos)
			{
 		        a=1;        
                        string ucid (templUserToUsr,loc);
			cout<<"\n location="<<loc ;
			cout<<"\n KASN ="<<ucid;
			lucid =ucid;
                        }
                        else
                        {
			cout<<" location="<<loc ;
			//lucid=ucid;
                        string ucid(templUserToUsr,loc);
			lucid=ucid;
                        }
			cout<<"\n UNDERTAKE ="<<lucid;
*/			
//if(ucid.compare(lUserToUser_old) == 0)
//{
//cout<<"KANE";
//}


/*const char *temp = ";";
int i = 0;
while( temp[i] != ';')
i++;*/
cout <<" AKASH lUserToUser_old = "<<lUserToUser_old;

cout <<"\n LENTH =" <<lUserToUser_old.length();

if(((lUserToUser_old.find ("00F")) != string::npos) &&  (((lUserToUser_old.find ("00F"))+3) < lUserToUser_old.length()))
{
      cout<<"\n LALAL ";
       lUserToUser_old.erase ( lUserToUser_old.begin(), lUserToUser_old.begin()+lUserToUser_old.find ("00F")+3);
}

if((lUserToUser_old.find (';')) != string::npos)
{
cout<<"SEMICOLON present in lUserToUser_OLD";
lUserToUser_old.erase ( lUserToUser_old.begin()+ lUserToUser_old.find (';'), lUserToUser_old.end());
}
       // lUserToUser_old.erase ( lUserToUser_old.begin()+ lUserToUser_old.find (';'), lUserToUser_old.end());
if(((lUserToUser.find ("00F")) != string::npos) && (((lUserToUser.find ("00F"))+3) < lUserToUser_old.length()))
if((lUserToUser.find ("00F")) != string::npos)
{
lUserToUser.erase ( lUserToUser.begin(), lUserToUser.begin()+lUserToUser.find ("00F")+3);
cout<<"\npresent ="<<lUserToUser;
}

if((lUserToUser.find (';')) != string::npos)
{
cout<<"SEMICOLON present in lUserToUser";
lUserToUser.erase ( lUserToUser.begin()+ lUserToUser.find (';'), lUserToUser.end());
cout<<"\n NNpresent = "<< lUserToUser;
}

/*cout<<"\n ANAN lUserToUser ="<<lUserToUser. c_str();
cout<<"\n ANAN lUserToUser_old ="<<lUserToUser_old . c_str();
cout << "\n compare " <<lUserToUser.compare (lUserToUser_old) <<endl;
//string sample = "00fabc";
//size_t a= sample.find(("00f"));
//cout <<"\n PRINT="<< (a+3);
*/



return 0;
}

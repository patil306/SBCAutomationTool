#include <iostream>
#include <string>

using namespace std;

int main()
{

    string userAuthPassword ="testuser123";
    string userPrivatePassword ="SBCEuser123";
    string UserAuthPassword_Modify =" ";
    string UserPrivatePassword_Modify= " ";

    cout<<"\n AerAuthPassword_Modify = "<<&UserAuthPassword_Modify;
    cout<<"\n UserPrivatePassword_Modify= "<<&UserPrivatePassword_Modify;
    
    int i,j;
    int a,b;
	 cout<<"\n KANE = "<<UserAuthPassword_Modify.c_str();
	 //cout<<"\n KANE ="<<UserPrivatePassword_Modify.c_str();
        for ( i=0, j=0; userAuthPassword[i]; i++)
        {
            if (userAuthPassword[i] == '$' || userAuthPassword[i] == '\\' || userAuthPassword[i] == '`' || userAuthPassword[i] == '"' )
            {
                        UserAuthPassword_Modify[j++] = '\\';
            }
        //    cout<<" \n 1 ####";
            UserAuthPassword_Modify[j++] = userAuthPassword[i];
        //    cout<<" \n IN UserAuthPassword_Modify= "<<UserAuthPassword_Modify.c_str()<<endl;
        }
         UserAuthPassword_Modify[j] = '\0';
         cout<<" \n 1 userAuthPassword ="<<userAuthPassword.c_str()<<endl;
         cout<<" \n 1 UserAuthPassword_Modify= "<<UserAuthPassword_Modify.c_str()<<endl;
	// cout<<"\n AKAS UserAuthPassword_Modify = "<<&UserAuthPassword_Modify;
	// cout<<"\n AKAS userAuthPassword = "<<&userAuthPassword;
	 //cout<<"\n AKAS userPrivatePassword = "<<&userPrivatePassword;
	 //cout<<"\n AKAS UserPrivatePassword_Modify = "<<&UserPrivatePassword_Modify;
         cout<<"\n 2 ****"<<UserPrivatePassword_Modify.c_str()<<endl;

//	string UserPrivatePassword_Modify;
	for ( a=0,b=0; userPrivatePassword[a]; a++)
        {
            if (userPrivatePassword[a] == '$' || userPrivatePassword[a] == '\\' || userPrivatePassword[a] == '`' || userPrivatePassword[a] == '"' )
            {
                        UserPrivatePassword_Modify[b++] = '\\';
            }
            UserPrivatePassword_Modify[b++] = userPrivatePassword[a];
        }
        UserPrivatePassword_Modify[b] = '\0';

        cout<<"\n ****"<<UserPrivatePassword_Modify.c_str()<<endl;
	cout<<"\n AKAS "<<&UserAuthPassword_Modify;
        cout<<"\n ####"<<UserAuthPassword_Modify.c_str()<<endl;
	cout<<"\n AKAS "<<&UserPrivatePassword_Modify;
} 

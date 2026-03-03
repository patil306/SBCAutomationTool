#include<iostream>
#include<fstream>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

using namespace std;

int main(int argc, char** argv)
{
	if(argc == 0 || argc < 8)
	{
		cerr<<"Invalid arguments";
		return -1;
	}
	string sbc_addr, ft_addr, numCalls;
	unsigned short set_delay, timestamp_delay, base_index;
	unsigned int numberofcalls;
	unsigned int sbc_start_port, ft_start_port;
	int c;
  opterr = 0;

  while ((c = getopt (argc, argv, "r:s:d:t:i:c:p:f:")) != -1)
  {
    switch (c)
      {
      case 'r':
		sbc_addr.assign( optarg);
		cout<<"sbc_Addr="<<sbc_addr<<"\n";
        break;
      case 's':
		ft_addr  = optarg;
		cout<<"ft_Addr="<<ft_addr<<"\n";
        break;
      case 'd':
        	set_delay = atoi(optarg);
		cout<<"SET_DELAY="<<set_delay<<"\n";
        break;

      case 't':
		timestamp_delay = atoi(optarg);
		cout<<"TIMESTAMP_DELAY"<<timestamp_delay<<"\n";
	break;
	
      case 'i':
		base_index = atoi(optarg);
		cout<<"BASE_INDEX"<<base_index<<"\n";
	break;

	case 'c':
		numberofcalls = atoi(optarg);		
		numCalls = optarg;
		cout<<"CALL"<<numberofcalls<<endl;

	break;

	case 'p':
		sbc_start_port = atoi(optarg);
		cout<<"SBC_PORT"<<sbc_start_port<<endl;	
	break;
	case 'f':
		ft_start_port = atoi(optarg);	
		cout<<"FT_PORT"<<ft_start_port<<endl;
	break;
	
      case '?':
	cout<<"HELP:"<<endl;
	cout<<"-r:SBC Receving side"<<endl;
	cout<<"-s:FT( sending side)"<<endl;
	cout<<"-d:Specifies delay between each consecutive RTP packets."<<endl;
	cout<<"-t:Timestamp field for each packet for same call_id"<<endl;
	cout<<"-i:starting value of the call index in this FT"<<endl;
	cout<<"-c:Number of calls"<<endl;
	cout<<"-p:Destination start port of SBC for"<<endl;
	cout<<"-f:source strat port of the FT"<<endl;
        return 1;
      default:
	cerr<<"Wrong input"<<endl;
        return -1;
      }
}
	//ofstream file;
	fstream file;
	unsigned int sbc_dest_port = sbc_start_port +2;
	unsigned int ft_src_port = ft_start_port +2;
	string file_name = "ft_" + numCalls + ".cfg";
	cout<<"FILE_NAME = "<<file_name<<endl;
	remove(file_name.c_str());
  	file.open (file_name.c_str(), fstream::in | fstream::out | fstream::app);
	  file <<"SBC_ADDRESS = "<<sbc_addr<<"\n";
	  file <<"FT_ADDRESS = "<<ft_addr<<"\n";
	  file <<"SET_DELAY = "<<set_delay<<"\n";
	  file <<"TIMESTAMP_DELAY = "<<timestamp_delay<<"\n";
	  file <<"BASE_INDEX = "<<base_index<<"\n";
	  file <<"CALL_0"<<"\n";
	  file <<"SBC_PORT = "<<sbc_dest_port<<"\n";
	  file<<"FT_PORT = "<<ft_src_port<<"\n";	
	  file<<"PACKET_REF_1 = "<<"1&2"<<"\n";
	  file<<"SEQ_NUM = "<<"25"<<"\n";
	  file<<"TIMESTAMP = "<<"50"<<"\n";
	  file<<"END_CALL"<<"\n";

	   sbc_dest_port +=2;
	   ft_src_port +=2;	
	  file <<"CALL_1"<<"\n";
	  file <<"SBC_PORT = "<<sbc_dest_port<<"\n";
	  file<<"FT_PORT = "<<ft_src_port<<"\n";	
	  file<<"PACKET_REF_1 = "<<"1&2"<<"\n";
	  file<<"SEQ_NUM = "<<"15"<<"\n";
	  file<<"TIMESTAMP = "<<"40"<<"\n";
	  file<<"END_CALL"<<"\n";

	for(int i = 2; i < numberofcalls*2 ; i++)
	{
		
  		file <<"CALL_"<<i<<"\n";
		if(i%2 == 0)
		{
			sbc_dest_port += 2;  	
  			file <<"SBC_PORT = "<<sbc_dest_port<<"\n";
			ft_src_port += 2;
			file<<"FT_PORT = "<<ft_src_port<<"\n";
		        file<<"PACKET_REF_1 = "<<"1&2"<<"\n";
		        file<<"SEQ_NUM = "<<"25"<<"\n";
		        file<<"TIMESTAMP = "<<"50"<<"\n";

		}
		else
		{
			sbc_dest_port += 2;
  			file <<"SBC_PORT = "<<sbc_dest_port<<"\n";
			ft_src_port += 2;
			file<<"FT_PORT = "<<ft_src_port<<"\n";
                        file<<"PACKET_REF_1 = "<<"1&2"<<"\n";
                        file<<"SEQ_NUM = "<<"25"<<"\n";
                        file<<"TIMESTAMP = "<<"50"<<"\n";
		}
		
		file<<"END_CALL"<<"\n";
	}

		ifstream ifile("payload", ios::in);
		if (!ifile.is_open()) {
 
                         cout << "file not found";
                             }
			     else
				{
					file<<ifile.rdbuf();
				}
			file<<"\n";
  file.close();
	
	return 0;
	
}

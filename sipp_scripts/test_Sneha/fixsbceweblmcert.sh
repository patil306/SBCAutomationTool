#!/bin/bash
#version 1.1 added manual webLM ip backup
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

echo "This script will import your WebLM certificate into your local truststore"
storep=`grep trustStorePassword /usr/local/weblm/etc/trustedcert.properties | cut -d= -f2`
deleteit=false
exists=`keytool -v -list -keystore /usr/local/weblm/etc/trusted_weblm_certs.jks -storepass $storep -noprompt | grep "Alias name: weblm$" -c`
if [ $exists == 1 ]; then
  if [[ $1 != "-delete" ]]; then
    echo -n "A trusted WebLM certificate already exists. Shall I delete it and replace it with the new WebLM certificate (Y/N)? [N] "
    read choice
    if [ `echo "$choice" | grep -ci "^y$"` -gt 0 ]; then
      deleteit=true
    else
      echo -e "\e[91mAborting...\e[0m"
      exit 1
    fi
  fi
fi

if [[ $1 == "-delete" ]] || [ $deleteit == true ]; then
  echo "Exporting existing WebLM certificate to /tmp/weblmbackup.pem"
  keytool -exportcert -file /tmp/weblmbackup.pem -alias weblm -keystore /usr/local/weblm/etc/trusted_weblm_certs.jks -storepass $storep
  echo "Deleting the weblm alias"
  keytool -delete -alias weblm -keystore /usr/local/weblm/etc/trusted_weblm_certs.jks -storepass $storep
  if [[ $1 == "-delete" ]]; then
    exit 1
  fi
fi

echo "Attempting to import the WebLM certs into the truststore..."
weblmIP=`sudo -u postgres psql commondb -c "select value from license_config where name like 'WEBLM_SERVER_URL';" | grep http | cut -d: -f2 | sed -r 's .{2}  '`

	if [[ $weblmIP != "" ]]; then
		echo "Using" $weblmIP "as WebLM ip"
	else
		echo "Failed to extract webLM ip from the database"
		echo "Enter the ip address of the webLM or SMGR you need to pull a certificate from"
		read weblmIP
	fi

cd /tmp
echo > /tmp/bothcerts.pem
echo > /tmp/bothcertsclean.pem

echo "Q" | openssl s_client -tls1_2 -showcerts -connect $weblmIP:52233 >> /tmp/bothcerts.pem 2>/dev/null
cat /tmp/bothcerts.pem | awk '/-----BEGIN CERTIFICATE-----/ {p=1}; p; /-----END CERTIFICATE-----/ {p=0}' >> /tmp/bothcertsclean.pem
keytool -import -trustcacerts -keystore /usr/local/weblm/etc/trusted_weblm_certs.jks -storepass $storep -alias weblm -file /tmp/bothcertsclean.pem  -noprompt

if [[ $? != 0 ]]; then
echo "If the alias already exists you can delete it with the -delete option"
fi

if [[ $1 == "-dontdelete" ]]; then
  echo "Certificate Files have been left in temp directory"
else
  rm /tmp/bothcerts.pem
  rm /tmp/bothcertsclean.pem
fi

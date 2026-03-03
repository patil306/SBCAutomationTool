confile=$1
echo $confile
confile=/home/pgokhe/venv/callflow/js-sequence-diagrams-master/config.py
if [ -z "$confile" ]
then
    echo "!!!!!!!Please provide confile as argument!!!!!!!"
else
    wssh --address='10.133.99.221' --port=8888 --policy=autoadd  --fbidhttp=False &
    python3 /home/pgokhe/venv/callflow/js-sequence-diagrams-master/app.py $confile &
    #python3 app_run.py $confile &
    python3 /home/pgokhe/venv/callflow/callflow_Template_Code/app.py $confile &
    python3 /home/pgokhe/venv/callflow/callflow_Template_Code/reportapp.py $confile &
    python3 /home/pgokhe/venv/callflow/homepage/homepage.py $confile &

fi

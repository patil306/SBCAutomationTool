echo "outside"
echo $2
exec >logfile.txt 2>&1
i=0
for ((n=0;n<$1;n++))
do
#	echo "echo"
	nohup python3 useragent.py -i $2 -r 10.133.39.157 -t -d bsnl.com -p 5060 -s 10 --clr 4002 --cle 4001 --uac &
	export pid_python=$!
	echo $pid_python
	echo "sleeping"
	sleep 10
	kill -s INT $pid_python
	kill -s INT $pid_python
	kill -s INT $pid_python
	kill -s INT $pid_python
	kill -s INT $pid_python
	kill -s INT $pid_python
        kill -s INT $pid_python
	kill -s INT $pid_python
#	kill -s $pid_python
	echo "Iteration $i done"
done


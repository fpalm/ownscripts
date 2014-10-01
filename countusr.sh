#!/bin/bash

USRNUM=0

for dir in $( ls /home/); do
	#echo $( ls /home/$dir | wc -w )
	USRNUM=$(($USRNUM + $( ls /home/$dir | wc -w )))
done

echo $USRNUM


#!/usr/bin/bash
day_of_week=`date +%a`;
time_now=`date +%0k%M`;
LINK=`awk -v systemday=$day_of_week -v systemtime=$time_now -v FMSP=0 -f gen_LINK.awk TT.csv`


#if [ "$LINK" != "" ]
#then
#echo $LINK
#`PATH TO BROWSER IN YOUR SYSTEM $LINK`
##gogle $LINK
#fi

if [ "$#" != 0 ]
then
	if [ "$1" == "FMSP" ]
	then
		LINK=`awk -v systemday=$day_of_week -v systemtime=$time_now -v FMSP=365 -f gen_LINK.awk TT.csv`
		#echo "ggehdfgzehb"
		echo $LINK
		`PATH TO BROWSER IN YOUR SYSTEM $LINK`
		exit
	fi

	if [ "$1" == "FNPTEL" ]
	then
		LINK=`awk -v systemday=$day_of_week -v systemtime=$time_now -v FMSP=599 -f gen_LINK.awk TT.csv`
		#echo "ggehdfgzehb"
		echo $LINK
		`PATH TO BROWSER IN YOUR SYSTEM $LINK`
		exit
	fi

	if [ "$1" == "CS2700" ]
	then
		LINK=`awk -v systemday=$day_of_week -v systemtime=$time_now -v FMSP=2700 -f gen_LINK.awk TT.csv`
		#echo "ggehdfgzehb"
		echo $LINK
		`PATH TO BROWSER IN YOUR SYSTEM $LINK`
		exit
	fi


	if [ "$1" == "ME2201" ]
	then
		LINK=`awk -v systemday=$day_of_week -v systemtime=$time_now -v FMSP=1100 -f gen_LINK.awk TT.csv`
		#echo "ggehdfgzehb"
		echo $LINK
		`PATH TO BROWSER IN YOUR SYSTEM $LINK`
		exit
	fi




	if [ "$1" == "RAM2200" ]
	then
		LINK=`awk -v systemday=$day_of_week -v systemtime=$time_now -v FMSP=2200 -f gen_LINK.awk TT.csv`
		#echo "ggehdfgzehb"
		echo $LINK
		`PATH TO BROWSER IN YOUR SYSTEM $LINK`
		exit
	fi






fi

if [ "$LINK" != "" ]
then
	if [ "$LINK" == "MA2020" ]
	then
		echo "No class for MA2020"
		exit
	elif [ "$LINK" == "EE1100" ]
	then
		echo "Check moodle for recorded lectures of EE1100"
		exit
	else
		echo $LINK
		`PATH TO BROWSER IN YOUR SYSTEM $LINK`
		#gogle $LINK
		exit
	fi
fi




if [ "$LINK" == "" ]
then
	echo "Either lunch break or no slot"
	exit
fi

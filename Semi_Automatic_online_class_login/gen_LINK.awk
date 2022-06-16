#!/usr/bin/gawk -f
BEGIN{
FS=",";
#systemtime="0805";    #Present time recieved from the system script
#systemday="Tue";
#outlink="";
#FMSP=0;
#print(systemtime);
#print(systemday);
};
{

if(FMSP==0){
	day=$1;
	stime=$3;
	etime=$4;
	link=$5;
	#print(systemday);
	#print(day);
	if(day==systemday){
		#print("wefrwew");
		if(systemtime>=stime && systemtime<=etime){
			outlink=link;
		#	print("trwereer");
		}
	}
}
#--------------------------#
if(FMSP==365){
	#print("ewfwefefw");
	if($1=="LINK_TO_AM2530_SPREADSHEET"){
		outlink=$5;
	}
}
#---------------------------------#
if(FMSP==599){
	if($1=="NPTEL_FLUIDS"){
		outlink=$5;
	}
}

#-------------------------#
if(FMSP==2700){
	if($1=="CS2700_YT"){
		outlink=$5;
	}
}

#-------------------------#


if(FMSP==1100){
	if($1=="ME1100_LEC"){
		outlink=$5;
	}
}

#------------------------------#

if(FMSP==2200){
	if($1=="RAM2200"){
		outlink=$5;
	}
}


};
END{
print(outlink);
};

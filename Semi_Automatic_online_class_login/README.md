This is a small autoation project that aims to automate the process of going to the online class login page. For eg, during the lockdown period we had online classes . There were a lot of links be it google meet link , zoom links , etc. This application was created using shell script and was run on WSL. 


This application used a main script to run an AWK script that generated a link that it read from a CSV file. The application used system time to find the correct link. All the information regarding timings was arranged in a proper manner in the CSV file.


All the links from the CSV file have been deleted. To run the application make sure to edit the file runner.sh and add 'PATH TO BROWSER IN YOUR SYSTEM' wherever mentioned in the file.

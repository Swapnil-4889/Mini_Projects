#!/usr/bin/python3
import sys
import os
import datetime
from datetime import date
def run():
	if (len(sys.argv) == 1):
		help()
	elif sys.argv[1] == 'help':
		help()
	elif sys.argv[1] == 'add':
		add(sys.argv[2])
	elif sys.argv[1] == 'ls':
		ls()
	elif sys.argv[1] == 'del':
		delete(sys.argv[2])
	elif sys.argv[1] == 'done':
		done(sys.argv[2])
	elif sys.argv[1] == 'report':
		report()

def help():
	print("Usage :-")
	print('$python3 todo.py add \"todo item\"        # Add a new todo ')
	print('$python3 todo.py ls        # Show remaining todos ')
	print('$python3 todo.py del NUMBER        # Delete a todo ')
	print('$python3 todo.py done NUMBER        # Complete a todo ')
	print('$python3 todo.py help        # Show Usage ')
	print('$python3 todo.py report        # Statistics ')

def add(a):
	f = open("todo.txt" , "a")
	f.writelines(a + "\n")
	f.close()
	print("Added to todo : "+a)

def ls():
	f = open("todo.txt","r")
	counter=0
	rcounter=0
	content = f.read()
	colist=content.split("\n")
	for i in colist:
		if i:
			counter +=1
	f.close();
	line = [""]*(counter+1)
	count = counter+1
	with open("todo.txt") as f:
		while True:
			count -=1
			line[count] = f.readline()
			if not line[count]:
				break

	f.close()
	d = counter
	for i in range(0,counter+1):
		if ((line[i] != "**\n") and (len(line[i]) > 0)):
			print("["+str(d)+"]"+" "+line[i].rstrip("\n"))
			d -=1



def delete(a):
	N =int(a)
	counterl = linecounter()
	if N>counterl:
		print("The entry number #"+str(N)+" does not exist. Nothing Deleted")
		return
	print("Deleted todo #"+str(N)+" from the file todo.txt")
	N = N - 1
	f = open("todo.txt" , "r")
	content = f.read()
	colist =content.split("\n")
	f.close()
	f = open("todo.txt" , "w")
	for items in range(0,counterl):
		if (items == N) :
			continue
		elif items < (counterl-1):
			f.write("%s\n" %colist[items])
		elif items == (counterl-1):
			f.write("%s\n" %colist[items])
	f.close()
	return str(colist[N])


def linecounter():
	f = open("todo.txt" , "r")
	counter=0
	content = f.read()
	colist=content.split("\n")
	for i in colist:
		if i:
			counter +=1
	f.close()
	return counter


def DONElinecounter():
        f = open("done.txt" , "r")
        counter=0
        content = f.read()
        colist=content.split("\n")
        for i in colist:
                if i:
                        counter +=1
        f.close()
        return counter



def done(a):
	Y = int(a)
	counterl = linecounter()
	if Y > counterl:
		print("todo #"+str(Y)+" does not exist")
		return
	P = delete(a)
	tofile = "x"+" "+ str(date.today()) +" "+P
	f= open("done.txt" , "a")
	f.writelines(tofile + "\n")
	f.close()
	print("Marked #"+str(Y)+" as done")

def report():
	current_time = datetime.datetime.now()
	dayi = str(current_time.day)+"/"
	monthi = str(current_time.month)+"/"
	year = str(current_time.year)
	day = dayi
	if (len(monthi) == 2):
		month = "0"+monthi
	else:
		month = monthi
	if (len(dayi) == 2):
		day = "0"+dayi
	else:
		day = dayi
	pending = str(linecounter())
	completed = str(DONElinecounter())
	DATE = day+month+year
	print(DATE+" "+"Pending : "+pending+" "+"Completed : "+completed)

run()

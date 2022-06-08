#!/usr/bin/python3
# coding: utf-8

# In[2]:


import numpy as np
import sys
#import math as math
from array import *
import re as RE
import pandas as pd
import dataframe_image as dfi

if(len(sys.argv) == 1):
	print('Please enter the controlled language text file as a command line input')
	exit()
else:
	filename=str(sys.argv[1])
# In[4]:


f = open(filename,'r')
Lines=f.readlines()
count=0
rows = []
for line in Lines:
    count +=1
    matched=bool(RE.search('has-row',line))
    if(matched):
        crow=line.split(' ')
        rows.append(crow[2].strip('\n'))
        


# In[5]:


# rows


# In[6]:


#A1=[""]*18
arr = []
#print(arr)


# In[7]:


#A1=[""]*18
#arr = []
#print(arr)

# r='Monday'
# count=0
# for line in Lines:
#     count +=1
#     matched=bool(RE.search(r+' has-slot',line))
#     if(matched):
#         crow=line.split(' ')
#         course=crow[2].strip('\n')
#         #print(course)
#         ctor=0
#         for L in Lines:
#             ctor +=1
#             m=bool(RE.search(course+' starts-at',L))
#             if(m):
#                 crew=L.split(' ')
#                 strstime=str(crew[2])
#                 #print(strstime)
#                 istime=int(strstime.split(':')[0])
#                 #print(istime)
#             n=bool(RE.search(course+' ends-at',L))
#             if(n):
#                 crew=L.split(' ')
#                 strstime=str(crew[2])
#                 ietime=int(strstime.split(':')[0])
#                 #print(ietime)
#             #print("istime",istime)
#             #print("ietime",ietime)
#         for al in range(istime,ietime):
#             A1[al]=course
            
# test=[]
# for n in range(8,18):
#     s=A1[n]
#     test.append(s)
# arr.insert(0,test)


# In[8]:


#A1=[""]*18
arr = []
#print(arr)

counter=0
for alp in rows:
    A1=[""]*18
    r=alp
    count=0
    for line in Lines:
        count +=1
        matched=bool(RE.search(r+' has-slot',line))
        if(matched):
            crow=line.split(' ')
            course=crow[2].strip('\n')
            #print(course)
            ctor=0
            for L in Lines:
                ctor +=1
                m=bool(RE.search(course+' starts-at',L))
                if(m):
                    crew=L.split(' ')
                    strstime=str(crew[2])
                    #print(strstime)
                    istime=int(strstime.split(':')[0])
                    #print(istime)
                n=bool(RE.search(course+' ends-at',L))
                if(n):
                    crew=L.split(' ')
                    strstime=str(crew[2])
                    ietime=int(strstime.split(':')[0])
                    #print(ietime)
                #print("istime",istime)
                #print("ietime",ietime)
            for al in range(istime,ietime):
                A1[al]=course

    test=[]
    for n in range(8,18):
        s=A1[n]
        test.append(s)
    arr.insert(counter,test)
    counter +=1


# In[9]:


#test


# In[10]:


#arr


# In[11]:


f.close()


# In[12]:


#arr[0][5]


# In[13]:


array=np.reshape(arr,(5,10))
#array


# In[14]:


data = {
    'Day' : rows,
    '8' : array[0:5,0],
    '9' : array[0:5,1],
    '10' : array[0:5,2],
    '11' :array[0:5,3],
    '12' :array[0:5,4],
    '13' :array[0:5,5] ,
    '14' :array[0:5,6],
    '15' :array[0:5,7],
    '16' :array[0:5,8],
    '17' :array[0:5,9],
    
}


# In[17]:


df=pd.DataFrame(data)
df


# In[16]:


print(df)
dfi.export(df, 'dataframe.png')


# # Lets See If it merges

# In[18]:


#array


# In[19]:


def Differ(l1,l2):
    test = [""]*10
    for n in range(0,10):
        if(l1[n] == l2[n]):
            test[n]=l1[n]
        else:
            test[n]=l1[n]+l2[n]
    out=bool(test==l1)
    return out


# In[20]:


# l1=array[0].tolist()
# l2=array[1].tolist()
# ll=Differ(l1,l2)
# ll


# In[21]:


# print(Differ(arr[1],arr[4]))


# In[23]:


print("\n\n")
count=1
for n in range(0,len(rows)):
    for j in range(count,len(rows)):
        test=Differ(arr[n],arr[j])
        if(test):
            print("Row ",(n+1)," can be merged with row ",(j+1),'')
        else:
            print("Row ",(n+1)," cannot be merged with row ",(j+1),'')
    count +=1
    


# In[ ]:





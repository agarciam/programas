#!/usr/bin/python
import os
import sys
import subprocess
from datetime import datetime, date, timedelta
from time import gmtime, strftime
import numpy as np


#range of days
s_day = 6
s_month = 1 
s_year = 1997

e_day = 29
e_month = 12
e_year = 2001


#calendar function
def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr, min(curr + delta, end)
        curr += delta


#market keywords
k= open('TICKERS3', "r")
key = k.readlines()
keyword = [item.rstrip('\n') for item in key]


#query for a close data 
markets = len(keyword) 
PRICES = []
RANDOM = []
week = [1, 2, 3, 4, 5]
for word in keyword:
    d = open( word + ".csv", "r")
    dat = d.readlines()
    datos = [item.split(',') for item in dat]
    dim =  np.shape(datos)
    n = dim[0]-1
    close =  [datos[i][4] for i in range(n)]
    dates =  [datos[i][0] for i in range(n)]
    CLOSE = []
    random = []
    j = 1
    k = 1
    l = 1
    #fill holes and avoid weekends
    for start, end in perdelta(date(s_year,s_month,s_day), date(e_year,e_month,e_day), timedelta(days=1)):
	m = k%7
	#print start.strftime('%Y-%m-%d'), dates[l-1]
	if  start.strftime('%Y-%m-%d') == dates[l-1]:
	    CLOSE.append(float(close[l-1]))
	    random.append(np.random.normal())
	    j+=1
	    l+=1
	elif m in week:
	    CLOSE.append(float(close[l-2]))
	    random.append(np.random.normal())
	    j+=1
	k+=1
    PRICES.append(CLOSE) 
    RANDOM.append(random)	 
    print (word,"t_days: " + str(len(CLOSE)), "holes: " + str(j-l), "ratio: " + str(round(100.0*(j-l)/len(CLOSE),2)) )
np.savetxt("RANDOM.txt", RANDOM, fmt='%.2f')        
np.savetxt("PRICES.txt", PRICES, fmt='%.2f')    
    
    

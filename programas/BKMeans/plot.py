#!/usr/bin/python
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates

with open(sys.argv[1], 'r') as d:
  dat = d.readlines()  
t = [item.split() for item in dat]

with open(sys.argv[2], 'r') as d:
  dat = d.readlines()  
serie = [item.split() for item in dat]




###Plot
dim_t = len(t)
time = np.zeros((dim_t))
SERIE = np.zeros((dim_t))
begin = 1992
end = 2010
lapse = 1.0*(end - begin + 1)/dim_t
step = 0
for i in range(dim_t):
    time[i] = step + 1.0*begin
    SERIE[i] = serie[i][0]
    step += lapse 
    print i,time[i],SERIE[i]



fig, ax = plt.subplots()
ax.plot(time, SERIE,'ko')
labels = ax.get_xticklabels()
for label in labels:
    label.set_rotation(45)

plt.xlim((begin,end))
plt.ylim((0,10))
plt.ylabel('States')
plt.title('Market States')

plt.savefig('STATES:N325_over40_lim10_nn10.png')






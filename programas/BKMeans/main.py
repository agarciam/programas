#!/usr/bin/python
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from functions import correlation
from functions import vectorize
from functions import BisectingKMeans
from functions import BisectingKMeans_realizations
from datetime import datetime


a = datetime.now()
###########################################################
###########################################################
### DATOS DE ENTRADA Y CONSTRUCCION DE MATRICES
###########################################################
###########################################################
###INPUT: Returns or Polarity Data (or Rudi data)

with open(sys.argv[1], 'r') as d:
  dat = d.readlines()  
data = [item.split() for item in dat]
data = np.transpose(data) #only for Rudi data (comment the line to other cases)
dim = np.shape(data)


###########################################################
###Temporal Correlation Matrices

T = 40  #two months
overlap = 5 #week
m = (dim[1] - T)/overlap + 1 #m matrices 
markets = 20#dim[0]

dataset =  [[[] for i in range(markets)] for j in range(m)]
for k in range(markets):
    for l in range(m):
	for i in range(T):
	    dataset[l][k].append(float(data[k][l+i]))    
	    

###########################################################
###Set of Correlation Matrices as SET of Vectors

SET = []
D = markets*(markets-1)/2
for I in xrange(m):
    matrix = []
    matrix  = dataset[I]
    V = []
    V = vectorize(correlation(matrix))
    SET.append(V)
ASET = np.asarray(SET)



###########################################################
###########################################################
### RESULTADOS (Seccion PARALELIZABLE!)
###########################################################
###########################################################
###Parametros Globales
threshold = 0.1
lim = 20
nn = 40
print "RESULTADOS..."
print
print dim,m,D

  
###########################################################  
### Resultados: 1ra biseccion
###########################################################

BKMR = BisectingKMeans_realizations(ASET, threshold, lim, nn)

ASET1 = BKMR[0]
ASET2 = BKMR[1]
LAB1  = BKMR[2]
LAB2  = BKMR[3]

print "1ra Biseccion:"
print LAB1
print LAB2
print "kk_ite =",BKMR[4] , ", mean_dist =",BKMR[5]
print


###########################################################
### Resultados: 2da biseccion
###########################################################
### 2da (I)

BKMR1 = BisectingKMeans_realizations(ASET1, threshold,lim, nn)

ASET11 = BKMR1[0] 
ASET12 = BKMR1[1]    
LAB11  = BKMR1[2]
LAB12  = BKMR1[3] 

print "2da Biseccion (I):"
print "relabel:"
RELAB11 = []
for i in range(len(LAB11)):
    RELAB11.append(LAB1[LAB11[i]])
print RELAB11
RELAB12 = []
for i in range(len(LAB12)):
    RELAB12.append(LAB1[LAB12[i]])
print RELAB12
print "kk_ite =",BKMR1[4], ", mean_dist =",BKMR1[5] 
print 

###########################################################
### 2da (II)

BKMR2 = BisectingKMeans_realizations(ASET2, threshold, lim,nn)

ASET21 = BKMR2[0] 
ASET22 = BKMR2[1]    
LAB21  = BKMR2[2]
LAB22  = BKMR2[3] 

print "2da Biseccion (II):"
print "relabel:"
RELAB21 = []
for i in range(len(LAB21)):
    RELAB21.append(LAB2[LAB21[i]])
print RELAB21
RELAB22 = []
for i in range(len(LAB22)):
    RELAB22.append(LAB2[LAB22[i]])
print RELAB22
print "kk_ite =",BKMR2[4], ", mean_dist =",BKMR2[5] 
print 


###########################################################
### Resultados: 3ra biseccion
###########################################################
### 3ra (I)

BKMR_I = BisectingKMeans_realizations(ASET11, threshold, lim,nn)

ASET_I1 = BKMR_I[0] 
ASET_I2 = BKMR_I[1]    
LAB_I1  = BKMR_I[2]
LAB_I2  = BKMR_I[3] 

print "3ra Biseccion (I):"
print "relabel:"
RELAB_I1 = []
for i in range(len(LAB_I1)):
    RELAB_I1.append(LAB1[LAB11[LAB_I1[i]]])
print RELAB_I1
RELAB_I2 = []
for i in range(len(LAB_I2)):
    RELAB_I2.append(LAB1[LAB11[LAB_I2[i]]])
print RELAB_I2
print "kk_ite =",BKMR_I[4], ", mean_dist =",BKMR_I[5] 
print 

###########################################################
### 3ra (II)

BKMR_II = BisectingKMeans_realizations(ASET12, threshold, lim, nn)

ASET_II1 = BKMR_II[0] 
ASET_II2 = BKMR_II[1]    
LAB_II1  = BKMR_II[2]
LAB_II2  = BKMR_II[3] 

print "3ra Biseccion (II):"
print "relabel:"
RELAB_II1 = []
for i in range(len(LAB_II1)):
    RELAB_II1.append(LAB1[LAB12[LAB_II1[i]]])
print RELAB_II1
RELAB_II2 = []
for i in range(len(LAB_II2)):
    RELAB_II2.append(LAB1[LAB12[LAB_II2[i]]])
print RELAB_II2
print "kk_ite =",BKMR_II[4], ", mean_dist =",BKMR_II[5] 
print 

###########################################################
### 3ra (III)

BKMR_III = BisectingKMeans_realizations(ASET21, threshold, lim, nn)

ASET_III1 = BKMR_III[0] 
ASET_III2 = BKMR_III[1]    
LAB_III1  = BKMR_III[2]
LAB_III2  = BKMR_III[3] 

print "3ra Biseccion (III):"
print "relabel:"
RELAB_III1 = []
for i in range(len(LAB_III1)):
    RELAB_III1.append(LAB2[LAB21[LAB_III1[i]]])
print RELAB_III1
RELAB_III2 = []
for i in range(len(LAB_III2)):
    RELAB_III2.append(LAB2[LAB21[LAB_III2[i]]])
print RELAB_III2
print "kk_ite =",BKMR_III[4], ", mean_dist =",BKMR_III[5] 
print 

###########################################################
### 3ra (IV)

BKMR_IV = BisectingKMeans_realizations(ASET22, threshold, lim, nn)

ASET_IV1 = BKMR_IV[0] 
ASET_IV2 = BKMR_IV[1]    
LAB_IV1  = BKMR_IV[2]
LAB_IV2  = BKMR_IV[3] 

print "3ra Biseccion (IV):"
print "relabel:"
RELAB_IV1 = []
for i in range(len(LAB_IV1)):
    RELAB_IV1.append(LAB2[LAB22[LAB_IV1[i]]])
print RELAB_IV1
RELAB_IV2 = []
for i in range(len(LAB_IV2)):
    RELAB_IV2.append(LAB2[LAB22[LAB_IV2[i]]])
print RELAB_IV2
print "kk_ite =",BKMR_IV[4], ", mean_dist =",BKMR_IV[5] 
print 

###########################################################
###########################################################
###GRAFICAR
###########################################################
###########################################################
print "GRAFICANDO..."
print
minimos = [min(RELAB_I1), min(RELAB_I2), min(RELAB_II1), min(RELAB_II2), \
	   min(RELAB_III1), min(RELAB_III2), min(RELAB_IV1), min(RELAB_IV2)]
states = np.argsort(minimos)

#print minimos
#print states

LABELS = []
LABELS.append(RELAB_I1)
LABELS.append(RELAB_I2)
LABELS.append(RELAB_II1)
LABELS.append(RELAB_II2)
LABELS.append(RELAB_III1)
LABELS.append(RELAB_III2)
LABELS.append(RELAB_IV1)
LABELS.append(RELAB_IV2)
#print LABELS[states[0]],LABELS[states[1]]


dim = []
for i in range(8):
    dim.append(len(LABELS[states[i]]))
t = range(0,m)
serie = np.zeros((m))
print dim
print
  
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0
i8 = 0
for i in range(m):
    if i1 < dim[0]:
      if i == LABELS[states[0]][i1]:
	serie[i] = 1  
	i1 += 1 
    if i2 < dim[1]:	 
      if i == LABELS[states[1]][i2]:
	serie[i] = 2
	i2 += 1
    if i3 < dim[2]:
      if i == LABELS[states[2]][i3]:
	serie[i] = 3  
	i3 += 1 
    if i4 < dim[3]:	 
      if i == LABELS[states[3]][i4]:
	serie[i] = 4
	i4 += 1    
    if i5 < dim[4]:
      if i == LABELS[states[4]][i5]:
	serie[i] = 5  
	i5 += 1 
    if i6 < dim[5]:	 
      if i == LABELS[states[5]][i6]:
	serie[i] = 6
	i6 += 1
    if i7 < dim[6]:
      if i == LABELS[states[6]][i7]:
	serie[i] = 7  
	i7 += 1 
    if i8 < dim[7]:	 
      if i == LABELS[states[7]][i8]:
	serie[i] = 8
	i8 += 1    	
	

plt.plot(t, serie,'ko') 
plt.ylim((0,10))
plt.xlabel('C(i)')
plt.ylabel('States')
plt.title('Market States')
plt.savefig('STATES.png')


b = datetime.now()
lapse = b-a
print ("time(s)= ", lapse.seconds)
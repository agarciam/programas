#!/usr/bin/python
import numpy as np
import random

###Cross-Correlation Matrix Function:
def correlation (data):
    dim = np.shape(data)
    N = dim[0]
    T = dim[1]
    matrix = []
    for k in range(N):
	row = []
	for l in range(T):
	    row.append(float(data[k][l]))
	rown = (row - np.mean(row))/np.std(row)
	matrix.append(rown)
    xirtam = np.transpose(matrix)
    C = 1.0/T*np.dot(matrix, xirtam)
    return C
 

  
  
###Vectorize Function:  
def vectorize (data):
    dim = np.shape(data)
    N = dim[0]
    T = dim[1]
    vector = []
    for k in range(N):
	for l in range(k+1,T):
	    vector.append(data[k][l])
    return vector



###########################################################
################ BISECTING FUNCTION #######################
###########################################################
### Funcion: 	BisectingKMeans
### in:  	ASET,threshold,lim
### out: 	SET1, SET2, LAB1, LAB2, kk, T1, T2
### SET1= 	Cluster 1
### SET2=	Cluster 2
### LAB1=	Etiquetas de tiempo donde C(i) in SET1
### LAB2=	Etiquetas de tiempo donde C(i) in SET2
### kk=		Numero limite de iteraciones permitidas
### T1,T=	Distancia promedio de los elementos de SET1 y SET2 a su centroide
###########################################################

def BisectingKMeans(ASET,threshold,lim):
    T1 = 10.0
    T2 = T1
    kk = 0


    ###Calcular Centroide Incial: Mu
    m = np.shape(ASET)[0]
    D = np.shape(ASET)[1]
    Mu = np.zeros((D))
    for i in range(D):
	for j in range(m):
	    Mu[i] += 1.0/m*ASET[j][i]


    ###Choose Two Initial Random Vectors of dim D around Mu 
    Mu1 = np.zeros((D))
    Mu2 = np.zeros((D))
    a = 0.01
    for i in range(D):
	Mu1[i] = Mu[i] + random.uniform(-a, a)
	Mu2[i] = Mu[i] - random.uniform(-a, a)
    LABELS = range(0, m)


    ###Start loop
    while ((T1  >= threshold) and (T2 >= threshold)):
  
      ###Re-asignar Centroides
      R1 = np.zeros((D))
      R2 = np.zeros((D))
      R1 = Mu1
      R2 = Mu2

  
      ###Calculate Distance Vecotors
      Vdis1 = np.zeros((m))
      Vdis2 = np.zeros((m))
      norm = (1.0/np.sqrt(D))
      for i in range(m):
	  Vdis1[i] = norm*np.linalg.norm(R1-ASET[i][:D])
	  Vdis2[i] = norm*np.linalg.norm(R2-ASET[i][:D])
   
 
      ###Create Two Initial Sets of Distances and Vectors
      DIS1 = [] 
      DIS2 = []
      SET1 = []
      SET2 = []
      LAB1 = []
      LAB2 = []
      for i in range(m):
	  if min(Vdis1[i], Vdis2[i]) == Vdis1[i]:
	      DIS1.append(Vdis1) 
	      SET1.append(ASET[i][:D])
	      LAB1.append(i)
	  else:
	      DIS2.append(Vdis2)  
	      SET2.append(ASET[i][:D])
	      LAB2.append(i)
  
  
      ###Condition: There is no change in labeling 
      if LAB1 == LABELS:
	  break
      LABELS = []  
      LABELS = LAB1

 
      ###Calcular Centroides
      ASET1 = np.asarray(SET1)
      ASET2 = np.asarray(SET2)
      N1 = len(DIS1)
      N2 = len(DIS2)
      Mu1 = np.zeros((D))
      Mu2 = np.zeros((D))
      for i in range(D):
	  for j in range(N1):
	      Mu1[i] += 1.0/N1*ASET1[j][i]
	  for j in range(N2):
	      Mu2[i] += 1.0/N2*ASET2[j][i]


      ###Calcular Threshold
      T1 = 0.0
      T2 = 0.0
      for j in range(N1):
	  T1 += 1.0/N1*norm*np.linalg.norm(Mu1-ASET1[j][:D])
      for j in range(N2):
	  T2 += 1.0/N2*norm*np.linalg.norm(Mu2-ASET2[j][:D])


      ###Condicion: Reiniciar valores
      if ((T1 == 0.0) or (T2 == 0)):
	T1 = 10.0
	T2 = T1
	Mu1 = np.zeros((D))
	Mu2 = np.zeros((D))
	for i in range(D):
	    Mu1[i] = Mu[i] + random.uniform(-a, a)
	    Mu2[i] = Mu[i] - random.uniform(-a, a)
	    continue


      ###Condicion: limite de iteraciones permitido
      kk +=1
      if kk == lim:
	break
   
    return ASET1, ASET2, LAB1, LAB2, kk, T1, T2


###########################################################
### BISECTINGKMEANS_realizations ##########################
###########################################################
### in: ASET, threshold, lim, nn
### nn = numero de realizaciones (indice PARALELIZABLE!) 
###Function to run BisectingKMeans over nn realizations
###and use which that  minimize mean distance: (T1 + T2)/2
###########################################################


def BisectingKMeans_realizations(ASET, threshold, lim, nn):
    aset1 = []
    aset2 = []
    label1 = []
    label2 = []
    kk_ite = []
    mean = np.zeros((nn))
    for i in range(nn):
      BKM = BisectingKMeans(ASET, threshold,lim)
      aset1.append(BKM[0])
      aset2.append(BKM[1])
      label1.append(BKM[2])
      label2.append(BKM[3])
      kk_ite.append(BKM[4])
      mean[i] =  (BKM[5] + BKM[6])/2.0 
    arg = np.argmin(mean)
    
    return aset1[arg], aset2[arg], label1[arg], label2[arg], kk_ite[arg], mean[arg]


  
    
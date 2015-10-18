##
##  Java Information Dynamics Toolkit (JIDT)
##  Copyright (C) 2012, Joseph T. Lizier
##  
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##  
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

# = Example 3 - Transfer entropy on continuous data using kernel estimators =
# Simple transfer entropy (TE) calculation on continuous-valued data using the (box) kernel-estimator TE calculator.

from jpype import *
import random
import math
import numpy as np
import readFloatsFile


#---------------------
# Change location of jar to match yours:
# 0. Set package
jarLocation = "infodynamics.jar"
# Start the JVM (add the "-Xmx" option with say 1024M if you get crashes due to not enough memory space)
startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=" + jarLocation)


#---------------------
# 1. Load in the data (loop for transfer matrix)
datafile1 = 'data/returns_sorted.txt'
data1 = readFloatsFile.readFloatsFile(datafile1)
A = np.array(data1)
C = np.transpose(A)
dim = np.shape(C)
t = dim[0]
n = dim[1]
print t,n

TRANSFER = np.zeros(shape=(n,n))
for j in range(n):
  for k in range(n):
    transfer = 0.0
    serie1 = [];
    serie2 = []
    for i in range(t):
      serie1.append(C[i,j])
      serie2.append(C[i,k])

##---------------------
## 2a. Create a TE calculator and run it: (KERNEL DENSITY)
    #teCalcClass = JPackage("infodynamics.measures.continuous.kernel").TransferEntropyCalculatorKernel
    #teCalc = teCalcClass();
    #teCalc.setProperty("NORMALISE", "true"); # Normalise the individual variables
    #teCalc.initialise(10, 0.8); # Use history length 1 (Schreiber k=1), kernel width of 0.5 normalised units

# 2b. Create a TE calculator and run it: (KRASKOV ESTIMATOR)
    teCalcClass = JPackage("infodynamics.measures.continuous.kraskov").TransferEntropyCalculatorKraskov
    teCalc = teCalcClass();
    teCalc.setProperty("NORMALISE", "true"); # Normalise the individual variables
    teCalc.initialise(1); # Use history length 1 (Schreiber k=1)
    teCalc.setProperty("k", "3"); # Use Kraskov parameter K=4 for 4 nearest points

#---------------------
# 3. Show results
    teCalc.setObservations(JArray(JDouble, 1)(serie1), JArray(JDouble, 1)(serie2));
    transfer = teCalc.computeAverageLocalOfObservations();
    #print(j,k,transfer);
    TRANSFER[j,k] = transfer 
 
np.savetxt("TransferBubble.txt",TRANSFER, fmt='%6.4f')   




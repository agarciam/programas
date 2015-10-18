#!/usr/bin/python
import os
import sys
import scipy.stats
import math 
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
import graphviz as gv


#Cross-Correlation Matrix Function:
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


##INPUT: Returns or Polarity Data
with open(sys.argv[1], 'r') as d:
  dat = d.readlines()  
data = [item.split() for item in dat]
C = correlation(data)
N = np.shape(C)
n = N[0]
#np.savetxt('CrossCorrelation.txt', C)
print N

##Distance Matrix (D)
D = np.zeros(N)
for i in range(n):
  for j in range(i,n):
    if j == i:
      D[i,i] = 0.0
    else:  
      D[i,j] = np.sqrt(2.0*(1.0-float(C[i][j])))    



#Minimum Spanninh Tree of distance matrix (D)
E = csr_matrix(D)
mst = minimum_spanning_tree(E)
MST = mst.toarray().astype('float')
np.savetxt("MST.txt", MST, fmt='%.2f')   


#################################DRAWING MST ##########################################
#######################################################################################
#To Netwrokx
G=nx.from_numpy_matrix(MST)
#G=nx.from_numpy_matrix(D)

graph_pos = nx.drawing.graphviz_layout(G,prog='neato')
node_size=1000
node_alpha=0.3
node_color='blue'
nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, alpha=node_alpha, node_color=node_color)

edge_tickness=0.5
edge_alpha=1
edge_color='blue'
nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,alpha=edge_alpha,edge_color=edge_color)


symbols={}
symbols[0]='MEX'
symbols[1]='US'
symbols[2]='ARG'
symbols[3]='BRA'
symbols[4]='UK'
symbols[5]='FRA'
symbols[6]='SWT'
symbols[7]='GER'
symbols[8]='AUT'
symbols[9]='EGY'
symbols[10]='ISR'
symbols[11]='IND' 
symbols[12]='INDO'
symbols[13]='MAL'
symbols[14]='SING'
symbols[15]='HKG'
symbols[16]='TWN'
symbols[17]='SKOR'
symbols[18]='JAP'
symbols[19]='AUS'
node_text_size=12
text_font='sans-serif'
nx.draw_networkx_labels(G, graph_pos,labels=symbols,font_size=node_text_size,font_family=text_font)



edge=nx.get_edge_attributes(G,'weight')
print edge
#weight = []
#for i in range(G.number_of_edges()):
    #weight.append(round(edge[G.edges()[i]],2))
#edge_labels = dict(zip(G.edges(), weight))    
#edge_text_pos=0.3
#nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, label_pos=edge_text_pos)

##save figure
plt.axis('off')
plt.show()
#plt.savefig('graph.png')
#plt.savefig('network.png')

####################################CONTINUE:############################################


#Shortes path of any two nodes
path = nx.shortest_path(G)


#Subdominant Heigh matrix (H)
H = np.zeros(N)
pdist = []
for k in range(n):
  for l in range(k,n):
    if k == l:
      H[k,l] = 0.0
    else:
      p = path[k][l]
      m = len(p)
      w = []
      for i in range(m-1):
	w.append(G[p[i]][p[i+1]]['weight'])
      H[k,l] = max(w)
      pdist.append(H[k,l])    
  

#To plot Dendrogram
link = linkage(pdist,'single')
countries = ["MEX","US","ARG","BRA","UK","FRA","SWT","GER","AUT","EGY","ISR", \
	     "IND","INDO","MAL","SING","HKG","TWN","SKOR","JAP","AUS"]
dend = dendrogram(link,labels=countries)
plt.xticks(rotation='vertical')



##save figure
plt.axis('on')
plt.ylim((0.4,1.4))
plt.ylabel('d<')
#plt.savefig('dendrogram.png')


 

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from networkx import * 
import numpy as np
with open ('Transfer.txt', 'r') as Transfer:
    Tra = Transfer.readlines()   
    T = [item.split() for item in Tra]
    
N= np.shape(T)
n = N[0]    
D = np.zeros(N)
#print type(D) 

for i in range(n): 
    for j in range(i,n):
	if T[i][j] > T[j][i]:
	  D[i,j] = T[i][j]
	  D[j,i] = 0.0
	else:
	  D[j,i] = T[j][i]
          D[i,j] = 0.0
          
#np.savetxt("D.txt", D, fmt='%.4f')   
    
#print type(D)    

graph = nx.DiGraph(D)
edge=nx.get_edge_attributes(graph,'weight')

inf=info (graph) 
print inf

out_node=DiGraph.out_degree(graph).values()
#print out_node
sort_out_index = np.argsort(out_node)[::-1]
#print sort_out_index
in_node=DiGraph.in_degree(graph).values()
#print in_node
sort_in_index = np.argsort(in_node)[::-1]
print ('out indices: ', sort_out_index)
print "--------------------------------------------------------------------------------------------------------------------------------------------"
print ('in indices: ', sort_in_index)

close_centra=closeness_centrality(graph, u=None, distance=None, normalized=True)
btw_centra=betweenness_centrality(graph, k=None, normalized=True, weight=None, endpoints=False, seed=None)
ev_cen=eigenvector_centrality(graph, max_iter=100, tol=1e-06, nstart=None, weight='weight')
print "Closeness Centrality"
print close_centra
print "Betweenneess Centrality"
print btw_centra
print "Eigenvector Centrality"
print ev_cen

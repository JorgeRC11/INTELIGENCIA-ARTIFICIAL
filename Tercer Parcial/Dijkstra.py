from modulefinder import packagePathMap
from struct import pack
import matplotlib.pyplot as plt
import networkx as nx
import random

G=nx.Graph()
nodos_G1=['A']
nodos_G2=['B','C','D']
nodos_G3=['E','F','G','H','I']
nodos_G4=['J','K','L','M','N']
nodos_G5=['O','P','Q','R','S']
nodos_G6=['T','U','V']
nodos_G7=['W']
G.add_nodes_from(nodos_G1,layer=1)
G.add_nodes_from(nodos_G2,layer=2)
G.add_nodes_from(nodos_G3,layer=3)
G.add_nodes_from(nodos_G4,layer=4)
G.add_nodes_from(nodos_G5,layer=5)
G.add_nodes_from(nodos_G6,layer=6)
G.add_nodes_from(nodos_G7,layer=7)

pos=nx.multipartite_layout(G,subset_key="layer")

aristas_G=[('A','B'),('A','C'),('A','D'),('B','F'),('B','E'),('B','I'),('B','G'),('B','H'),('C','E'),('C','G'),('D','G'),('D','H'),('E','J'),('E','L'),('F','K'),('F','J'),('F','M'),('G','K'),('G','M'),('H','L'),('H','N'),('I','M'),('I','N'),('J','O'),('J','Q'),('K','P'),('K','O'),('K','R'),('L','Q'),('L','S'),('M','R'),('M','S'),('N','Q'),('N','S'),('O','T'),('P','T'),('Q','U'),('R','V'),('S','U'),('T','W'),('U','W'),('V','W'),('B','C'),('F','E'),('G','H'),('H','I'),('I','K'),('M','P'),('J','P'),('O','P'),('S','V'),('Q','V'),('T','U'),('U','V'),('D','I'),('C','H'),('G','J'),('Q','T'),('P','U'),('C','D'),('G','L'),('R','S'),('Q','R'),('F','G'),('P','Q')]

def add_edges(G,u,v,n,c):
	
	G.add_edge(u,v,color=c,weight=n)


for j in range(0,len(aristas_G)):
		n= random.randint(50,150)
		add_edges(G,aristas_G[j][0],aristas_G[j][1],n,'b')
		aristas_G[j]=aristas_G[j]+(n,)

best=nx.dijkstra_path(G, 'A', 'W')
print(best)


E=nx.Graph()
nodos_G1=['A']
nodos_G2=['B','C','D']
nodos_G3=['E','F','G','H','I']
nodos_G4=['J','K','L','M','N']
nodos_G5=['O','P','Q','R','S']
nodos_G6=['T','U','V']
nodos_G7=['W']
E.add_nodes_from(nodos_G1,layer=1)
E.add_nodes_from(nodos_G2,layer=2)
E.add_nodes_from(nodos_G3,layer=3)
E.add_nodes_from(nodos_G4,layer=4)
E.add_nodes_from(nodos_G5,layer=5)
E.add_nodes_from(nodos_G6,layer=6)
E.add_nodes_from(nodos_G7,layer=7)
pos=nx.multipartite_layout(E,subset_key="layer")

costo=0
for j in range(0,len(aristas_G)):
	x=aristas_G[j][0]
	y=aristas_G[j][1]
	if (x in best) and (y in best):
		add_edges(E,aristas_G[j][0],aristas_G[j][1],aristas_G[j][2],'r')
		costo=costo+aristas_G[j][2]
	else:
		add_edges(E,aristas_G[j][0],aristas_G[j][1],aristas_G[j][2],'b')
print('El valor del camino de menor resistencia electrica es de: ',costo)

colors=nx.get_edge_attributes(E,'color').values()
labels=nx.get_edge_attributes(E,'weight')
nx.draw_networkx_edge_labels(E,pos,edge_labels=labels,label_pos=0.2,font_size=8)
nx.draw_networkx(E,pos,edge_color=colors)
plt.show()

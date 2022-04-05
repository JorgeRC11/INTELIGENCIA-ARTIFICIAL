import matplotlib.pyplot as plt
import networkx as nx

G=nx.Graph()
nodos_G1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']

nodos_G2=['CARRERA_1', 'CARRERA_2', 'CARRERA_3', 'CARRERA_4' , 'CARRERA_5']

nodos_G3=['C1_1','C1_2','C1_3','C1_4','C1_5', 'C2_1','C2_2','C2_3','C2_4','C2_5', 'C3_1','C3_2','C3_3','C3_4','C3_5', 'C4_1','C4_2','C4_3','C4_4','C4_5', 'C5_1','C5_2','C5_3','C5_4','C5_5']
nodos_G4=['CARRERA_6']
nodos_G5=['C6_1','C6_2','C6_3','C6_4','C6_5']
nodos_G6=['CX_1','CX_2','CX_3','CY_1','CY_2']
nodos_G7=['CARRERA_7']
nodos_G8=['P1','P2']
G.add_nodes_from(nodos_G1,layer=1)
G.add_nodes_from(nodos_G2,layer=2)
G.add_nodes_from(nodos_G3,layer=3)
G.add_nodes_from(nodos_G4,layer=4)
G.add_nodes_from(nodos_G5,layer=5)
G.add_nodes_from(nodos_G6,layer=6)
G.add_nodes_from(nodos_G7,layer=7)
G.add_nodes_from(nodos_G8,layer=8)
#G.add_nodes_from(nodos_G9,layer=9)


aristas_G=[ ('A', 'CARRERA_1'),('B', 'CARRERA_1'),('C', 'CARRERA_1'),('D', 'CARRERA_1'),('E', 'CARRERA_1'),('F', 'CARRERA_2'),('G', 'CARRERA_2'),('H', 'CARRERA_2'),('I', 'CARRERA_2'),('J', 'CARRERA_2'),('K', 'CARRERA_3'),('L', 'CARRERA_3'),('M', 'CARRERA_3'),('N', 'CARRERA_3'),('O', 'CARRERA_3'),('P', 'CARRERA_4'),('Q', 'CARRERA_4'),( 'R', 'CARRERA_4'),('S', 'CARRERA_4'),('T', 'CARRERA_4'),('U', 'CARRERA_5'),('V', 'CARRERA_5'),('W', 'CARRERA_5'),('X', 'CARRERA_5'),('Y', 'CARRERA_5'),('C1_1', 'CARRERA_1'),('C1_2', 'CARRERA_1'),('C1_3', 'CARRERA_1'),('C1_4', 'CARRERA_1'),('C1_5', 'CARRERA_1'), ('C2_1', 'CARRERA_2'),('C2_2', 'CARRERA_2'),('C2_3', 'CARRERA_2'),('C2_4', 'CARRERA_2'),('C2_5', 'CARRERA_2'), ('C3_1', 'CARRERA_3'),('C3_2', 'CARRERA_3'),('C3_3', 'CARRERA_3'),('C3_4', 'CARRERA_3'),('C3_5', 'CARRERA_3'),( 'C4_1', 'CARRERA_4'),('C4_2', 'CARRERA_4'),('C4_3', 'CARRERA_4'),('C4_4', 'CARRERA_4'),('C4_5', 'CARRERA_4'), ('C5_1', 'CARRERA_5'),('C5_2', 'CARRERA_5'),('C5_3', 'CARRERA_5'),('C5_4', 'CARRERA_5'),('C5_5', 'CARRERA_5'),( 'C1_1', 'CARRERA_6'), ( 'C2_1','CARRERA_6'), ('C3_1', 'CARRERA_6'), ('C4_1','CARRERA_6'), ('C5_1', 'CARRERA_6'),( 'CARRERA_6', 'C6_1'), ( 'CARRERA_6', 'C6_2'), ( 'CARRERA_6', 'C6_3'), ( 'CARRERA_6', 'C6_4'), ( 'CARRERA_6', 'C6_5'),( 'C6_1', 'CX_1'), ( 'C6_1', 'CX_2'), ( 'C6_1', 'CX_3'), ( 'C6_2', 'CY_1'), ( 'C6_2', 'CY_2'), ( 'CX_1','CARRERA_7'), ( 'CX_2','CARRERA_7'), ( 'CX_3','CARRERA_7'), ( 'CY_1','CARRERA_7'), ( 'CY_2','CARRERA_7'),( 'CARRERA_7', 'P1'),( 'CARRERA_7', 'P2')]
layers=[('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','U','V','W','X','Y'),( 'CARRERA_1', 'CARRERA_2', 'CARRERA_3', 'CARRERA_4' , 'CARRERA_5'),( 'C1_1','C1_2','C1_3','C1_4','C1_5', 'C2_1','C2_2','C2_3','C2_4','C2_5', 'C3_1','C3_2','C3_3','C3_4','C3_5', 'C4_1','C4_2','C4_3','C4_4','C4_5', 'C5_1','C5_2','C5_3','C5_4','C5_5'),( 'CARRERA_6'),( 'C6_1','C6_2','C6_3','C6_4','C6_5'),( 'CX_1','CX_2','CX_3','CY_1','CY_2'),( 'CARRERA_7'),( 'P1','P2')]
G.add_edges_from(aristas_G)
pos=nx.multipartite_layout(G,subset_key="layer")
nx.draw_networkx_nodes(G,pos,node_size=200)
nx.draw_networkx_edges(G,pos,edgelist=G.edges(),edge_color='black')
nx.draw_networkx_labels(G,pos)
plt.show()

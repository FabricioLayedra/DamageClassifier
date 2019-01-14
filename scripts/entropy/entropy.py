import networkx as nx
import matplotlib.pyplot as plt
import sys
from math import log2
### execute with: python degree_difference.py graph_filename 

def normalized_topological_entropy(pairs_volumes,total_volume):
	"""Based on the metric of the same name, in the paper Network Diversity and Economic Development, by Eagle et al."""
	entropy = 0
	total_volume = total_volume if total_volume>1 else total_volume+1
	for pair,vij_volume in pairs_volumes:
		result= (int(vij_volume)/total_volume)*log2(int(vij_volume)/total_volume)
		#print(int(vij_volume)/total_volume)
		entropy+=result
	entropy = -entropy
	entropy = entropy/log2(total_volume) 
	return entropy


#open and read the graph file
file1 = sys.argv[1]

fh=open(file1, 'rb')
fh.readline()
cdrs_net_1 = nx.read_edgelist(fh, create_using=nx.DiGraph(), delimiter=",",data=(('weight',float),))
fh.close()


#for u, v, d in cdrs_net_1.edges(data=True):
    #print(d['weight'])

#Generate a file with the description of both graphs
dscrpt_file = open("output/description.txt","w")
N, K = nx.number_of_nodes(cdrs_net_1), nx.number_of_edges(cdrs_net_1)
description = "Grafo "+file1+"\n"
description += "Num nodos:"+str(N)+"\n"
description+= "Num arcos:"+str(K)+"\n"
avg_deg = K/float(N)
description += 'average degree ' + str(avg_deg)+"\n"
dscrpt_file.write(description)
dscrpt_file.close()

#Get a list of the edges of the graph, in the form (node1,node2)
edges_list = list(cdrs_net_1.edges)
#
past_node = edges_list[0][0]
past_pair = edges_list[0][1]
vij_volume = 0 #total call volumes of a single pair (i,j)
sum_vij_volume = 0 #total call volumes for tower i
entropies_pairs = dict()
total_volumes = dict()

for edge in edges_list:
	current_node = edge[0]
	current_pair = edge[1]
	print(past_node+' '+past_pair+' '+current_node+' '+current_pair)
	if(current_node == past_node):
		#we are with the same node i
		if(current_pair==past_pair):
			#we are with the same pair (i,j)
			vij_volume+=1
		else:
			#its a new j node
			entropies_pairs[(current_node,past_pair)] = vij_volume
			vij_volume = 1
		sum_vij_volume+=1
	else:
		#its a new pair (i,j), so all the volumes must be reset to 1, not zero because this new pair counts as 1
		total_volumes[past_node] = {"pairs_volumes":entropies_pairs,"total_volume":sum_vij_volume}
		sum_vij_volume = 1
		vij_volume = 1
		entropies_pairs = dict()
	past_node = current_node
	past_pair = current_pair

entropies = dict()
#Get the entropy of nodes in the graph
for node,volumes in total_volumes.items():
	entropy = normalized_topological_entropy(volumes["pairs_volumes"],volumes["total_volume"])
	entropies[node] = entropy
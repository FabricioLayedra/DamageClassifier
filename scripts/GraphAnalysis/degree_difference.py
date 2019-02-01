import networkx as nx
import matplotlib.pyplot as plt
import sys

### execute with: python degree_difference.py filename1 filename2

#open and read the 2 graph files
file1 = sys.argv[1]
file2 = sys.argv[2]

fh=open(file1, 'rb')
fh.readline()
cdrs_net_1 = nx.read_edgelist(fh, create_using=nx.DiGraph(), delimiter=",",data=(('weight',float),))
fh.close()

fh2=open(file2, 'rb')
fh2.readline()
cdrs_net_2 = nx.read_edgelist(fh2, create_using=nx.DiGraph(), delimiter=",", data=(('weight',float),))
fh2.close()

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


n,k=nx.number_of_nodes(cdrs_net_2),nx.number_of_edges(cdrs_net_2)
description += "Grafo "+file2+"\n"
description += "Num nodos:"+str(n)+"\n"
description+= "Num arcos:"+str(k)+"\n"
avg_deg = k/float(n)
description += 'average degree ' + str(avg_deg)+"\n"
dscrpt_file.write(description)
print(description)
dscrpt_file.close()

#Get the indegrees of nodes in both graphs
in_degrees_graph_1 = dict(cdrs_net_1.in_degree(weight="weight"))
in_degrees_graph_2 = dict(cdrs_net_2.in_degree(weight="weight"))

#write in degrees results for graph 1

results1 = open("output/in_degrees_graph_1.csv", "w")
results1.write("GeoId,InDegree\n")
for k,v in in_degrees_graph_1.items():
	line = k+","+str(v)+"\n"
	print(line)
	results1.write(line)
results1.close()

#write in degrees results for graph 2
results2 = open("output/in_degrees_graph_2.csv", "w")
results2.write("GeoId,InDegree\n")
for k,v in in_degrees_graph_2.items():
	line = k+","+str(v)+"\n"
	print(line)
	results2.write(line)
results2.close()



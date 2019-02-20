import networkx as nx
import sys
import os

"""
Command-line : python3 calculate_pagerank.py graph_file centrality_scores_file
This script computes a personalized page rank, based on an importance score, given by the centrality_scores_file.
centrality_scores_file can be, e.g: in_degrees_file with the csv format node,in_degree.
"""
graph_file = sys.argv[1]
ranks_filename = sys.argv[2]

#read the tower ranks file and create a dictionary
ranks_file = open(ranks_filename,"r")
ranks_file.readline()
personalization = {}
for line in ranks_file:
	data = line.strip().split(",")
	node = data[0]
	rank = float(data[1])
	personalization[node] = rank
ranks_file.close()

#read the graph file
fh=open(graph_file, 'rb')
fh.readline()
cdrs_net = nx.read_edgelist(fh, create_using=nx.DiGraph(), delimiter=",",data=(('weight',float),))
fh.close()

#compute page rank with personalized starting probabilities
pagerank_scores = dict(nx.pagerank(cdrs_net, personalization = personalization))

#write results
path = graph_file.split("/")
if(len(path)>1):
	path = "/".join(path[:-1])+"/towerRank"
else:
	path = path + "/towerRank"
if not os.path.exists(path):
    os.makedirs(path)

output_file = open(path+"/tower_ranks.csv","w")
output_file.write("GeoId,TowerRank\n")
for node,rank in pagerank_scores.items():
	output_file.write(str(node)+","+str(rank)+"\n")
output_file.close()
print(path+"/tower_ranks.csv")
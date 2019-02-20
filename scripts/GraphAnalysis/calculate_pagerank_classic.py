import networkx as nx
import sys
import os

"""
Command-line : python3 calculate_pagerank.py graph_file output_path
This script computes the pagerank of nodes
"""
graph_file = sys.argv[1]

fh=open(graph_file, 'rb')
fh.readline()
cdrs_net = nx.read_edgelist(fh, create_using=nx.DiGraph(), delimiter=",",data=(('weight',float),))
fh.close()

#compute page rank with personalized starting probabilities
pagerank_scores = dict(nx.pagerank(cdrs_net))

path = sys.argv[2]

output_file = open(path,"w")
output_file.write("GeoId,TowerRank\n")
for node,rank in pagerank_scores.items():
	output_file.write(str(node)+","+str(rank)+"\n")
output_file.close()

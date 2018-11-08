To generate a graph:
1)run calculate_distances.py : this file add a distance column, which is the distance in km between the home and client tower
2)get_edges: generates a file with nodes and edges, from the file with the distance column resulted from 1)
3)degree_difference: creates two graphs, using the files resulted from 2), and computes the degrees of the nodes in both graphs. 
4)analyze_in_degree: using the files from 2), it transforms them to pandas Dataframes, and analyzes, for example, degrees distributions

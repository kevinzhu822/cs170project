


import networkx as nx 
from itertools import combinations, chain
from networkx.utils import pairwise, not_implemented_for
from networkx.algorithms import approximation
# from networkx.algorithms.approximation import min_weighted_dominating_set
# import networkx as nx
from parse import read_input_file, write_output_file, read_output_file
from utils import is_valid_network, average_pairwise_distance
import sys
import os


def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """

    # TODO: your code here!
    # T1 = G.copy()
    # if DegreeCheck(G):
    # 	return G

    if (G.number_of_nodes() == 2):
    	T2 = nx.Graph()
    	T2.add_node(0)

    if (G.number_of_nodes() == 1):
    	T2 = nx.Graph()
    	T2.add_node(0)
    	return T2
    
    else:
	    dominating_set = nx.dominating_set(G)
	    # print(dominating_set)
	    copy = G.copy()
	    # for edge in G.edges():
	    # 	firstVertex = edge[0]
	    # 	secondVertex = edge[1]
	    # 	if firstVertex and secondVertex in dominating_set:
	    # 		copy.remove_edge(firstVertex, secondVertex)
	    # 		print(firstVertex, secondVertex)
	    # print("hi")
	    # print(copy.edges())
	    # T2 = copy.subgraph(dominating_set)
	    # print(T2.edges())
	    T2 = steiner_tree(G, dominating_set)
	    # print(T2.edges)
	    # T = nx.minimum_spanning_tree(copy)
	    # T2 = removeLeaves(T)
	    # print(T2)
	    # T2 = copy

    return T2
    
def DegreeCheck(G):
	numNodes = G.number_of_nodes()

	for node in G.nodes():
		counter = 0
		for neighbor in G.neighbors(node):
			counter +=1

		if counter == numNodes - 1:
			G.clear()
			G.add_node(node)
		return True
	return False

def metric_closure(G, weight='weight'):
    """  Return the metric closure of a graph.

    The metric closure of a graph *G* is the complete graph in which each edge
    is weighted by the shortest path distance between the nodes in *G* .

    Parameters
    ----------
    G : NetworkX graph

    Returns
    -------
    NetworkX graph
        Metric closure of the graph `G`.

    """
    M = nx.Graph()

    Gnodes = set(G)

    # check for connected graph while processing first node
    all_paths_iter = nx.all_pairs_dijkstra(G, weight=weight)
    u, (distance, path) = next(all_paths_iter)
    if Gnodes - set(distance):
        msg = "G is not a connected graph. metric_closure is not defined."
        raise nx.NetworkXError(msg)
    Gnodes.remove(u)
    for v in Gnodes:
        M.add_edge(u, v, distance=distance[v], path=path[v])

    # first node done -- now process the rest
    for u, (distance, path) in all_paths_iter:
        Gnodes.remove(u)
        for v in Gnodes:
            M.add_edge(u, v, distance=distance[v], path=path[v])

    return M



def steiner_tree(G, terminal_nodes, weight='weight'):
    """ Return an approximation to the minimum Steiner tree of a graph.

    Parameters
    ----------
    G : NetworkX graph

    terminal_nodes : list
         A list of terminal nodes for which minimum steiner tree is
         to be found.

    Returns
    -------
    NetworkX graph
        Approximation to the minimum steiner tree of `G` induced by
        `terminal_nodes` .

    Notes
    -----
    Steiner tree can be approximated by computing the minimum spanning
    tree of the subgraph of the metric closure of the graph induced by the
    terminal nodes, where the metric closure of *G* is the complete graph in
    which each edge is weighted by the shortest path distance between the
    nodes in *G* .
    This algorithm produces a tree whose weight is within a (2 - (2 / t))
    factor of the weight of the optimal Steiner tree where *t* is number of
    terminal nodes.

    """
    # M is the subgraph of the metric closure induced by the terminal nodes of
    # G.
    M = metric_closure(G, weight=weight)
    # Use the 'distance' attribute of each edge provided by the metric closure
    # graph.
    H = M.subgraph(terminal_nodes)
    mst_edges = nx.minimum_spanning_edges(H, weight='distance', data=True)
    # Create an iterator over each edge in each shortest path; repeats are okay
    edges = chain.from_iterable(pairwise(d['path']) for u, v, d in mst_edges)
    T = G.edge_subgraph(edges)
    return T
def removeLeaves(G):

	vertexOccurences = {}

	for edge in G.edges(data = True):
		firstVertex = edge[0]
		secondVertex = edge[1]


		if firstVertex in vertexOccurences:
			vertexOccurences[firstVertex] += 1

		else:
			vertexOccurences[firstVertex] = 1


		if secondVertex in vertexOccurences:
			vertexOccurences[secondVertex] += 1

		else:
			vertexOccurences[secondVertex] = 1


	verticesToBeRemoved = []
	for vertex in vertexOccurences:
		if vertexOccurences[vertex] == 1:
			#remove this vertex
			verticesToBeRemoved.append(vertex)


	for vertex in verticesToBeRemoved:
		G.remove_node(vertex)
	return G



# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G = read_input_file(path)
#     T = solve(G)
#     # print(read_output_file(path, G))
#     print(T.edges())
#     assert is_valid_network(G, T)
   
#     print("Average pairwise distance: {}".format(average_pairwise_distance(T)))
#     write_output_file(T, 'out/test2.out')

if __name__ == "__main__":
    output_dir = "outputs"
    input_dir = "inputs"
    total_distance = 0 
    for input_path in os.listdir(input_dir):
        print(input_path)
        graph_name = input_path.split(".")[0]
        G = read_input_file(f"{input_dir}/{input_path}")
        T = solve(G)
        if not (T.number_of_nodes() == 0):
            total_distance += average_pairwise_distance(T)
            print(total_distance)
        # print(input_path)
            assert is_valid_network(G, T)
        write_output_file(T, f"{output_dir}/{graph_name}.out")
    print("Average pairwise distance total: {}".format(total_distance))




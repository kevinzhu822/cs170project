import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_network, average_pairwise_distance
import sys


def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """

    # TODO: your code here!
    # T1 = G.copy()
    if DegreeCheck(G):
    	return G

    T = nx.minimum_spanning_tree(G)
    T2 = removeLeaves(T)

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


def removeLeaves(G):
	# print(G.edges(data = True))
	
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


	# print(vertexOccurences)
	

	verticesToBeRemoved = []
	for vertex in vertexOccurences:
		if vertexOccurences[vertex] == 1:
			#remove this vertex
			verticesToBeRemoved.append(vertex)

	# newEdges = []


	# for edge in G.edges(data = True):
	# 	if edge[0] not in verticesToBeRemoved and edge[1] not in verticesToBeRemoved:
	# 		newEdges.append(edge)
	# 	else:
	# 		pass


	for vertex in verticesToBeRemoved:
		G.remove_node(vertex)

	# print(G.edges())
	# print(G.nodes())
	return G



# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G = read_input_file(path)
    T = solve(G)
    assert is_valid_network(G, T)
    print("Average pairwise distance: {}".format(average_pairwise_distance(T)))
    write_output_file(T, 'out/test3.out')

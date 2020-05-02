from parse import *
import networkx as nx
import os
import solver

def solve(G):
    """
    Args:
        G: networkx.Graph

    Returns:
        T: networkx.Graph
    """

    # TODO: your code here!
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


if __name__ == "__main__":
    output_dir = "outputs"
    input_dir = "inputs"
    for input_path in os.listdir(input_dir):
        graph_name = input_path.split(".")[0]
        G = read_input_file(f"{input_dir}/{input_path}")
        T = solve(G)
        write_output_file(T, f"{output_dir}/{graph_name}.out")




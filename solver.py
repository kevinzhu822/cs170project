import networkx as nx
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
    T1 = G.copy()
    output = DegreeCheck(G)
    if output[0]:
    	T2 = nx.Graph()
    	T2.add_node(output[1])
    	return T2

    if (G.number_of_nodes() == 2):
    	T2 = nx.Graph()
    	T2.add_node(0)
    
    else:

	    T = nx.minimum_spanning_tree(G)
	    T2 = removeLeaves(T)

    return T2
    
def DegreeCheck(G):
	numNodes = G.number_of_nodes() -1

	# for node in G.nodes():
	# 	counter = 0
	# 	for neighbor in G.neighbors(node):
	# 		counter +=1

	# 	if counter == numNodes - 1:
	# 		G.clear()
	# 		G.add_node(node)
	# 	return True
	# return False
	for node in G.nodes():
		if len(list(G.neighbors(node))) == numNodes:
			return (True, node)
	return(False, numNodes)


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
#     assert is_valid_network(G, T)
   
#     print("Average pairwise distance: {}".format(average_pairwise_distance(T)))
#     write_output_file(T, 'out/test2.out')

if __name__ == "__main__":
    output_dir = "outputs"
    input_dir = "inputs"
    for input_path in os.listdir(input_dir):
        graph_name = input_path.split(".")[0]
        G = read_input_file(f"{input_dir}/{input_path}")
        T = solve(G)

        # print(read_output_file(input_path, G))
        assert is_valid_network(G, T)
        write_output_file(T, f"{output_dir}/{graph_name}.out")

# if __name__ == "__main__":
#     output_dir = "outputs"
#     input_dir = "inputs"
#     total_distance = 0 
#     for input_path in os.listdir(input_dir):
#         print(input_path)
#         graph_name = input_path.split(".")[0]
#         G = read_input_file(f"{input_dir}/{input_path}")
#         T = solve(G)
#         if not (T.number_of_nodes() == 0):
#             total_distance += average_pairwise_distance(T)
#             print(total_distance)
#         # print(input_path)
#             assert is_valid_network(G, T)
#         write_output_file(T, f"{output_dir}/{graph_name}.out")
#     print("Average pairwise distance total: {}".format(total_distance))

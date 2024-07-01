# Initialization for testing Graph class
num_vertices = 5
edges = [(0,1), (0,4), (1,2), (1,3), (1, 4), (2,3), (3,4)]
new_edge = (0,3)

class Graph:
    """Class that represents a graph with vertices and edges as well as displaying those connections via ASCII"""
    def __init__(self, num_vertices, edges):
        # Initialize number of vertices
        self.num_vertices = num_vertices
        # Create a list of empty list of size num_vertices
        self.data = [[] for _ in range(num_vertices)]
        # Add an edges into their corresponding vertices
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    
    # Function that adds an edge bewteen two vertices
    def add_edge(self, n1, n2):
        self.data[n1].append(n2)
        self.data[n2].append(n1)

    # Function that removes an edges bewteen two vertices
    def remove_edge(self, n1, n2):
        self.data[n1].remove(n2)
        self.data[n2].remove(n1)

    def __repr__(self):
        return "\n".join(["{} -> {}".format(vertex, neighbors) for vertex, neighbors in enumerate(self.data)])
    
    def __str__(self):
        return self.__repr__()

# Tests for Graph class
# graph1 = Graph(num_vertices, edges)
# graph1.add_edge(0,3)
# graph1.remove_edge(2,3)
# print(graph1)

class AdjacencyMatrix:
    """Class that represents an Adjacency Matrix via creating a table of 0's with size of num _vertices by num_vertices"""
    def __init__(self, num_vertices, edges):
        # Initialize the amount of vertices
        self.num_vertices = num_vertices
        # Create a table with size num_vertices by num_vertices populating the table with all zeros
        self.data = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        # If two vertices have an edge connecting to them then increment the corresponding cell by 1
        for n1, n2 in edges:
            self.data[n1][n2] = 1
            self.data[n2][n1] = 1

    def __repr__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])
    
    def __str__(self):
        return self.__repr__()

# Tests for AdjacencyMatrix class
# graph1 = AdjacencyMatrix(num_vertices, edges)
# print(graph1)

def bfs_performer(graph, root, discovered):
    """Performs breadth-first search by taking a graph and a root node as input"""
    # Initialize a queue and as well as a index that will go through each element in the queue
    queue, idx = [], 0
    # Initialize the distance each node is from the root node (at first setting all distances to None)
    distance = [None] * len(graph.data)
    # Initialize the parent list (initially setting each nodes parent to be none)
    parent = [None] * len(graph.data)
    # Have the root node be discovered (Turned from false discovered to true discovered)
    discovered[root] = True
    # Append the root to the queue
    queue.append(root)
    # Initialize the distance from the root node to itself (which is 0)
    distance[root] = 0
    # Initialize variable that checks if a graphs nodes are all connected by an edge
    # (Initially being True)
    connected = True
    # Iterate through the queue
    while idx < len(queue):
        # Get the currently selected element in the queue and increment the index by 1
        current = queue[idx]
        idx += 1
        # Check all the adjacent nodes of the currently selected element
        for adjacent_node in graph.data[current]:
            # If the adjacent node has yet been discovered
            if not discovered[adjacent_node]:
                # Update the distance by 1 plus the distances of the other nodes that have already been discovered
                distance[adjacent_node] = 1 + distance[current]
                # Mark the adjacent nodes parent as the root node
                parent[adjacent_node] = current
                # Mark the adjacent node as discovered
                discovered[adjacent_node] = True
                # Add the adjacent node to the queue
                queue.append(adjacent_node)

    # Check if the length of the queue matches the length of edges to check if the graphs nodes are connected
    if len(queue) != len(graph.data):
        connected = False

    # Return the queue, the distances, the parent nodes, as well as if the graph is connected
    return queue, distance, parent, connected

def component_tracker(graph):
    """Function that tracks the amount of sub-components there are in a graph via bfs"""
    # Initialize a counter that tracks the amount of components
    components = 0
    # Initialize the discovered list for each node (originally setting each discovered node to be False)
    discovered = [False] * len(graph.data)

    # Iterate through each node in the graph
    for node in range(len(graph.data)):
        # If the node is not discovered
        if not discovered[node]:
            # Perfrom the bfs
            bfs_performer(graph, node, discovered)
            # Increment the component counter by 1
            components += 1

    # Return the amount of components there were in the graph
    return components

# Wrapper function of bfs_performer that returns a default discovered list as well as root node, for user usage 
def bfs(graph, root):
    """Wrapper function that returns necessary parameters for bfs_performer function"""
    discovered = [False] * len(graph.data)
    return bfs_performer(graph, root,discovered)
 
# Testing for bfs & component tracker function 
# num_nodes3 = 9
# edges3 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
# graph1 = Graph(num_vertices, edges)
# print(bfs(graph1, 3))
# print(f"Num of Components in Graph:", component_tracker(graph1))

def dfs(graph, root):
    """Function that performs Depth-First search via inputs of a graph and a root node"""
    # Initialize a stack and the result which will store the traversal in-order
    stack, result = [], []
    # Initialize the parent list (initially setting each nodes parent to None)
    parent = [None] * len(graph.data)
    # Initialize the discovered list, (initially each nodes discovery is set to false)
    discovered = [False] * len(graph.data)
    # Append the root node to the stack
    stack.append(root)
    
    # Iterate though the stack 
    while len(stack) > 0:
        # Pop the last node from the stack initializing it as the current node
        current = stack.pop()
        # Check if the current node (the node that just got popped) is not already discovered
        if not discovered[current]:
            # Mark the current node as discovered
            discovered[current] = True
            # Append the current node to the resulting list
            result.append(current)
            # For each adjacent node from the current node
            for adjacent_node in graph.data[current]:
                # If the adjacent node has not already been discovered, append it to the stack
                if not discovered[adjacent_node]:
                    stack.append(adjacent_node)
                    # Mark the current node as the parent to the adjacent node
                    parent[adjacent_node] = current
                    

    # Return the resulting list in the order the nodes were discovered, along with the parent nodes 
    return result, parent

# Testing for dfs function
# graph1 = Graph(num_vertices, edges)
# print(dfs(graph1, 3))

def dfs2(graph, root, target):
    """Another version of Depth-First Search that is able to find all possible paths from a root node to a target node, taken from a leetcode problem"""
    # Initialize the stack as a tuple containing the root node, and the path that the algorithm 
    # traversed through (initially the path is only the root node)
    stack = [(root, [root])]
    # Initialize the resulting list
    result = []
    
    # While the stack is not empty
    while stack:
        # Pop the last node from the stack which contains the node and the path taken to get to the node
        # Initiallizing the node as "current", and the path taken as "path"
        (current, path) = stack.pop()

        # If the current node is equal to the target
        if current == target:
            # Add the path taken to the root node to the result
            result.append(path)
        else:
            # For each adjacent node of the current node 
            for adjacent_node in graph[current]:
                # If the adjacent node is not already in the path
                if adjacent_node not in path:
                    # Append the adjacent node along with updating the path that took to get to it
                    stack.append((adjacent_node, path + [adjacent_node]))
    
    # Return the result
    return result
        
# Testing for dfs2 function on DAGs
dag = [[1,2],[3],[3],[]]
dag2 = [[4,3,1],[3,2,4],[3],[4],[]]
print(dfs2(dag2, 0, 4))

class Graph2: 
    """Class that represents mutiple types of graphs (weighted, unweighted, directed, and undirected)"""
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        # Represents an index for adjacent nodes that correspond to a specific node
        self.data = [[] for _ in range(num_nodes)]
        # Represents an index for weights that correspond to a specific node
        self.weight = [[] for _ in range(num_nodes)]

        # For each edge
        for edge in edges:
            # If weighted is true
            if self.weighted:
                # Initialize the adjacent nodes and the weight that corresponds to them
                node1, node2, weight = edge
                # Add node2 to the adjacency list of node1
                self.data[node1].append(node2)
                # Add the corresponding weight to the weight list of node1
                self.weight[node1].append(weight)
                # If the graph is not directed, add an edge from node2 to node1 with the same corresponding weight
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)

            # Else if weighted is not True
            else:
                # Get the corresponding nodes (without weight)
                node1, node2 = edge
                # Add node2 to the adjacency list of node1
                self.data[node1].append(node2)
                # If graph is not directed
                if not directed:
                    # Add node1 to the adjacency list of node2
                    self.data[node2].append(node1)

    def __repr__(self):
        # Initialize the resulting string
        result = ""
        # If the graph is weighted
        if self.weighted:
            # Iterate over each node
            for node in range(self.num_nodes):
                # Add the node and its corresponding edges (self.data has the nodes edges) 
                # with weights to the resulting string
                result += "{}: {}\n".format(node, list(zip(self.data[node], self.weight[node])))
        # If the graph is not weighted
        else:
            # Iterate over each node
            for node in range(self.num_nodes):
                # Add the node and its edges to the resulting string
                result += "{}: {}\n".format(node, self.data[node])
        # Return the resulting string
        return result
    
# Testing for Graph2 class
# num_nodes2 = 9
# edges2 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
            # (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

# num_nodes3 = 4
# edges3 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]

# num_nodes4 = 5
# edges4 = [(0, 1, 2), (1, 2, 1), (2, 3, 2), (2, 4, 4), (4 , 2, 6), (3, 0, 1)]
  
# graph2 = Graph2(num_nodes4, edges4, directed=True, weighted=True)
# print(graph2)

def shortest_path(graph, root, target):
    """Function that performs shortest path algorithm of a graph based on the value of its weights"""
    # Initialize each node in the graph as unvisited (False)
    vistited = [False] *  len(graph.data)
    # Initialize the distance of edges as infinity
    distance = [float("inf")] * len(graph.data)
    # Initialize a queue as a list for adding and removing nodes
    queue = []
    # Initialize parent list that stores a nodes parent (orignally setting each nodes parent to None)
    parent = [None] * len(graph.data)
    # Initialize an index to go through each node in the graph
    idx = 0
    # Mark the distance to the root node as zero (since the root node has a distance of zero to itself)
    distance[root] = 0
    # Add the root node to the queue
    queue.append(root)

    # Iterate though the queue and check if the target has not been visited
    while idx < len(queue) and not vistited[target]:
        # Get the current node by getting the current index in the queue
        current = queue[idx]
        # Mark the current node as visited   
        vistited[current] = True
        # Move on to the next node in the queue
        idx += 1
        # Update the distances of all the adjacent nodes by comparing smallest distances via helper function
        update_distances(graph, current, distance, parent)
        # Find the first unvisited node with the smallest distance by using another helper function
        next_node = pick_next_node(distance, vistited)

        # If there is a node whos distance is smaller than other distances in the iteration
        if next_node:
            # Append that next node to the queue
            queue.append(next_node) 

    # Return the distance of the target (the distances from the root node to the target node) and the parent nodes
    return distance[target], parent

def update_distances(graph, current, distance, parent=None):
    """Helper function for shortest path function that updates the distances of adjacent nodes in a graph per iteration"""
    # Initialize the adjacent nodes that connect to the current node
    adjacent_nodes = graph.data[current]
    # Grab the weights of the adjacent node(s)
    weights = graph.weight[current]

    # Initialize an index as well as the adjacent node
    for idx, adjacent in enumerate(adjacent_nodes):
        # Initialize the weight of the corresponding edge of the adjacent node
        weight = weights[idx]
        # If the distance to the current node plus the weight of the edge is less than the known distance to the adjacent node
        if distance[current] + weight < distance[adjacent]:
            # Update the distance of the adjacent node
            distance[adjacent] = distance[current] + weight
            # If a parent dictionary is provided (If the parent is set to True on the parameters)
            if parent:
                # Update the parent of the adjacent node be the current node
                parent[adjacent] = current

def pick_next_node(distance, visited):
    """Helper function for smallest path function that picks a new node in a graph based on if a nodes distance/weight is the smallest"""
    # Initialize the smallest distance as infinity (all distances that have not been found are automatically set to infinity)
    smallest_distance = float("inf")
    # Initialize the smallest node as None 
    smallest_node = None

    # Loop through each node's distance
    for node in range(len(distance)):
            # If the node has not been visted and the nodes distance is less than the currently known smallest distance
            if not visited[node] and distance[node] < smallest_distance:
                # Update the smallest node and smallest distance
                smallest_node = node
                smallest_distance = distance[node]

    # Return the smallest node
    return smallest_node

# Testing for shortest path function and along with the two helper functions
# num_nodes5 = 6
# edges5 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]

# num_nodes2 = 9
# edges2 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          #(2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

# graph3 = Graph2(num_nodes2, edges2, weighted=True)
# print(shortest_path(graph3, 2, 8))
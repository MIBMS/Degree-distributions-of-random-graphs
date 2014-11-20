'''First part is some example graphs. 2nd is a function making a complete n graph,
3rd is a function that makes a node-degree dictionary, 4th is a function that 
makes a degree-number of nodes with degree dictionary'''


EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([7,3]), 3: set([7]), 4: set([1]), 5: set([2]), \
            6: set([]), 7: set([3]), 8: set([1,2]), 9: set([0,4,5,6,7,3])}
            
def make_complete_graph(num_nodes):
    '''Takes the number of nodes num_nodes and returns a dictionary corresponding 
    to a complete directed graph with the specified number of nodes. A complete graph 
    contains all possible edges subject to the restriction that self-loops are not allowed.
    The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is positive.
    Otherwise, the function returns a dictionary corresponding to the empty graph. '''
    if num_nodes > 0:
        complete_graph = {}
        for node in range(num_nodes):
            list_to_be_set = []
            for other in range(num_nodes):
                if other != node:
                    list_to_be_set.append(other)
            complete_graph[node] = set(list_to_be_set)
        return complete_graph
    else:
        return {}
        
def ve_graph(digraph):
    '''Takes a digraph in the form of adjacency list of vertices and adjacent vertices, and makes a vertex and edge set for the graph'''
    vlist = []
    elist = []
    for node in digraph:
        vlist.append(node)
        for adj_node in digraph[node]:
            elist.append((node,adj_node))
    return vlist, elist

def compute_in_degrees(digraph):
    '''Takes a directed graph digraph (represented as a dictionary) 
    and computes the in-degrees for the nodes in the graph. The function 
    should return a dictionary with the same set of keys (nodes) as digraph whose
    corresponding values are the number of edges whose head matches a particular node.'''
    
    vlist, elist = ve_graph(digraph)
    
    in_degree_count = {}
    for node in vlist:
        in_degree_count[node] = 0
    for _, innode in elist:
        in_degree_count[innode] += 1
    return in_degree_count

    
def in_degree_distribution(digraph):
    '''Takes a directed graph digraph (represented as a dictionary) and computes 
    the unnormalized distribution of the in-degrees of the graph. The function 
    should return a dictionary whose keys correspond to in-degrees of nodes in 
    the graph. The value associated with each particular in-degree is the number 
    of nodes with that in-degree. In-degrees with no corresponding nodes in the 
    graph are not included in the dictionary.'''   
    
    in_degree_count = compute_in_degrees(digraph)
    degree_dist = {}
    for node in in_degree_count:
        #if a degree is not in degree_dist
        if in_degree_count[node] not in degree_dist:
            #add a new entry in the degree - number of nodes dictionary, a new degree
            degree_dist[in_degree_count[node]] = 1
        else:
            degree_dist[in_degree_count[node]] += 1
    return degree_dist


        
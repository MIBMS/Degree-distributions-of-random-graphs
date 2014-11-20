import DPAtrial as dpa
import itertools

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
        
def DPAgraph(n, m):
    '''Creates a DPA graph with n vertices and initialized with a complete
    graph on m vertices'''
    graph = make_complete_graph(m)
    #creates a DPA simulator using DPATrial class, which updates itself 
    #DPATrial class is called once, then each call of run_trial will
    #update the sample space V from which the m nodes are chosen. V is initialized
    #to range(m)
    DPAsim = dpa.DPATrial(m)
    for i in range(m, n):        
        #adjvset is V' which is set of vertices adjacent to i
        adjvset = DPAsim.run_trial(m)
        graph[i] = set()
        for adj_node in adjvset:
            graph[i].add(adj_node)
    return graph

def DPAgraphve(n,m):
    '''Takes a digraph in the form of adjacency list of vertices and adjacent vertices, and makes a vertex and edge set for the graph'''
    digraph = DPAgraph(n,m)
    vset = set()
    eset = set()
    for node in digraph:
        vset.add(node)
        for adj_node in digraph[node]:
            eset.add((node,adj_node))
    return vset, eset
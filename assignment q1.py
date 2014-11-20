"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2

# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

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
    
def normalized_distribution(digraph):
    '''normalizes the degree sequence'''
    degree_dist = in_degree_distribution(digraph)
    count_node = sum(degree_dist.values())
    normalized_dictionary = {}
    for degree in degree_dist:
        normalized_dictionary[degree] = float(degree_dist[degree])/float(count_node)
    return normalized_dictionary


citation_graph = load_graph(CITATION_URL)

#degree_dist = in_degree_distribution(citation_graph)

normalized_dictionary = normalized_distribution(citation_graph)


import matplotlib.pyplot as plt
plt.plot(normalized_dictionary.keys(), normalized_dictionary.values(), 'ro')



#plt.axis([1, 100, -10, 0])
#plt.xscale('log')
#plt.yscale('log')
plt.title('In-degree Distribution of Physics Papers')
plt.xlabel('In-degree of author')
plt.ylabel('Probability of author having in-degree')
plt.show()


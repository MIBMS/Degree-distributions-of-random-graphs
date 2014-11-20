import DPAtrial as dpa
import itertools

def make_complete_graph(num_nodes):
    '''Takes the number of nodes num_nodes and returns a dictionary corresponding 
    to a complete directed graph with the specified number of nodes. A complete graph 
    contains all possible edges subject to the restriction that self-loops are not allowed.
    The nodes of the graph should be numbered 0 to num_nodes - 1 when num_nodes is positive.
    Otherwise, the function returns a dictionary corresponding to the empty graph. '''
    
    def findsubsets(S,m):
        '''finds all ordered 2-tuples of S'''
        return set(itertools.permutations(S, m))
        
    if num_nodes > 0:
        vset = set(range(num_nodes))
        eset = set()
            
        
        for pairtuple in findsubsets(vset, 2):
            elt1 = pairtuple[0]
            elt2 = pairtuple[1]
            if elt1 != elt2:
                eset.add(pairtuple)
        
        return vset, eset
    
    else:
        return set(), set()
        
def DPAgraph(n, m):
    '''Creates a DPA graph with n vertices and initialized with a complete
    graph on m vertices'''
    graph = make_complete_graph(m)
    vset = graph[0]
    eset = graph[1]
    #creates a DPA simulator using DPATrial class, which updates itself 
    #DPATrial class is called once, then each call of run_trial will
    #update the sample space V from which the m nodes are chosen. V is initialized
    #to range(m)
    DPAsim = dpa.DPATrial(m)
    for i in range(m, n):        
        #adjvset is V' which is set of vertices adjacent to i
        adjvset = DPAsim.run_trial(m)
        vset.add(i)
        for adj_node in adjvset:
            eset.add((i, adj_node))
    return vset, eset
    
    
def compute_in_degrees(digraph):
    '''Takes a directed graph digraph (represented as a dictionary) 
    and computes the in-degrees for the nodes in the graph. The function 
    should return a dictionary with the same set of keys (nodes) as digraph whose
    corresponding values are the number of edges whose head matches a particular node.'''
    
    vlist = digraph[0]
    elist = digraph[1]
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
    
def plotDPAgraph(n,m):
    '''plots a DPA graph with parameters n, m'''
    normalized_dictionary = normalized_distribution(DPAgraph(n,m))
    import matplotlib.pyplot as plt
    plt.plot(normalized_dictionary.keys(), normalized_dictionary.values(), 'ro')

    #plt.axis([1, 100, -10, 0])
    plt.xscale('log')
    plt.yscale('log')
    plt.title('Log/log plot of in-degree Distribution of DPA Graph, n = %s, m=%s' % (n,m))
    plt.xlabel('Log base 10 of in-degree of node')
    plt.ylabel('Log base 10 of probability of node having in-degree')
    plt.show()    
    
    
import itertools
import random



def ERalg(n, p):
    '''ER algorithm takes n and p and produces a directed graph with n vertices.
    Each possible edge (2 nC2 of them) is considered and added to edge set with
    probability 0<=p<=1'''
    
    vset = set(range(n))
    eset = set()
    
    def findsubsets(S,m):
        '''finds all ordered 2-tuples of S'''
        return set(itertools.permutations(S, m))
        
    for pairtuple in findsubsets(vset, 2):
        elt1 = pairtuple[0]
        elt2 = pairtuple[1]
        if elt1 != elt2:
            randomnumber = random.random()
            if randomnumber < p:
                eset.add(pairtuple)

                
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
    
    
def plotERgraph(n,p):
    '''plots an ER graph in G(n,p)'''
    normalized_dictionary = normalized_distribution(ERalg(n,p))
    import matplotlib.pyplot as plt
    plt.plot(normalized_dictionary.keys(), normalized_dictionary.values(), 'ro')

    #plt.axis([1, 100, -10, 0])
    #plt.xscale('log')
    #plt.yscale('log')
    plt.title('In-degree Distribution of ER Graph, n = %s, p=%s' % (n,p))
    plt.xlabel('In-degree of node')
    plt.ylabel('Probability of node having in-degree')
    plt.show()
    
def plotnormal(mean, sigma):
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.mlab as mlab

    x = np.linspace(440,560,100)
    plt.plot(x,mlab.normpdf(x,mean,sigma))
    plt.title('Normal distribution, mean = %s, s.d.=%s' % (mean,sigma))
    plt.xlabel('Value of random variable')
    plt.ylabel('Probability density of random variable')
    plt.show()

    plt.show()
    
plotERgraph(1000,0.1)
plotERgraph(1000,0.5)
plotERgraph(1000,0.9)
plotnormal(500, 250**0.5)
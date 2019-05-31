import numpy as np
import random
import networkx as nx
from time import time
from numba import jit

# N listas, una para cada jugador, cada una tiene M listas correspondientes
# a cada objecto, y las formas de llamarlos dentro de cada lista


def extract_allwithall(N):
    """
    -----------------
    Input
            the number of nodes N
    -----------------
    Output
            a vector of N elements
                each element containing all neighbours of the corresponding node
                according to the structure of complete graph (mean field)
    -----------------
    """
    neighs = [[] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                neighs[i].append(j)
    return np.asarray(neighs)

def extract_neigh_square(N):
    """
    -----------------
    Input
            the number of nodes N
    -----------------
    Output
            a vector of N elements
                each element containing all neighbours of the corresponding node
                according to the structure of a square lattice (2D)
    -----------------
    """
    L=int(np.sqrt(N))
    sites=np.arange(L*L).reshape(L,L)
    neighs=[[] for i in range(L*L)]
    for i in range(L):
        for j in range(L):
            neighs[sites[i,j]].extend((sites[(i+1)%L,j],sites[i,(j+1)%L],sites[(i-1)%L,j],sites[i,(j-1)%L]))
    return np.asarray(neighs)

def extract_small_world(N,k,p):
    """
    -----------------
    Inputs
            N: the number of nodes
            k: the number of neighbours of each node
            p: the probability of rewiring
    -----------------
    Output 
             a vector of N elements
                each element containing all neighbours for its corresponding node
                according to the structure of the Watts-Strogatz model (small world)
    -----------------
    """
    G=nx.watts_strogatz_graph(N, k, p)

    neighs=[[] for i in range(N)]
    for i in G.edges:
        neighs[i[0]].append(i[1])
        neighs[i[1]].append(i[0])
    return np.asarray(neighs)

def extract_scalefreeBA(N,m):
    G=nx.barabasi_albert_graph(N,m)
    neighs=[[] for i in range(N)]
    for i in G.edges:
        neighs[i[0]].append(i[1])
        neighs[i[1]].append(i[0])
    return np.asarray(neighs)

def extract_social():
    G = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)
    N = len(G.nodes)
    neighs=[[] for i in range(N)]
    for i in G.edges:
        neighs[i[0]].append(i[1])
        neighs[i[1]].append(i[0])
    return N, np.asarray(neighs)

def extract_social_zealots():
    G = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)
    N = len(G.nodes)
    neighs=[[] for i in range(N)]
    for i in G.edges:
        neighs[i[0]].append(i[1])
        neighs[i[1]].append(i[0])

    zealots = []
    
    #ordered by degrees
    grados = G.degree()
    listgrad = [grados[i] for i in range(N)]
    for i in range(400):
        indice = listgrad.index(max(listgrad))
        zealots.append(indice)
        del[listgrad[indice]]
    
    """
    #ordered randomly
    for i in range(40):
        indice = np.random.randint(N)
        if indice not in zealots:
            zealots.append(indice)
    
    #ordered by betweeness
    centrals = nx.betweenness_centrality(G, normalized=True)#, endpoints=True)
    listcentr = [centrals[i] for i in range(N)]
    for i in range(40):
        indice = listcentr.index(max(listcentr))
        zealots.append(indice)
        del[listcentr[indice]]
    """
    return N, zealots, np.asarray(neighs)


def step(N, neighs, inventary):
    success_rate = 0
    for i in range(N):
        ##normal order
        speaker = np.random.randint(N)
        hearer = np.random.choice(neighs[speaker])
        ##reversed order for BA comparison
        #hearer = np.random.randint(N)
        #speaker = np.random.choice(neighs[hearer])

        if len(inventary[speaker]) == 0:
            inventary[speaker].append(np.random.choice(10**5))

        definicion_speaker = np.random.choice(inventary[speaker])
        success = False
        for objs in inventary[hearer]:
            if objs == definicion_speaker:
                success = True

        if success:  # success
            inventary[speaker] = [definicion_speaker]
            inventary[hearer] = [definicion_speaker]
            success_rate += 1

        if not success:  # failure
            inventary[hearer].append(definicion_speaker)

    success_rate /= float(N)
    return inventary, success_rate

def step_zealots(N, zealots, neighs, inventary):
    success_rate = 0
    for i in range(N):
        ##normal order
        speaker = np.random.randint(N)
        hearer = np.random.choice(neighs[speaker])
        ##reversed order for BA comparison
        #hearer = np.random.randint(N)
        #speaker = np.random.choice(neighs[hearer])

        if len(inventary[speaker]) == 0:
            inventary[speaker].append(np.random.choice(10**5))

        definicion_speaker = np.random.choice(inventary[speaker])
        success = False
        for objs in inventary[hearer]:
            if objs == definicion_speaker:
                success = True

        if success:  # success
            inventary[speaker] = [definicion_speaker]
            inventary[hearer] = [definicion_speaker]
            success_rate += 1

        if hearer not in zealots:
            if not success:  # failure
                inventary[hearer].append(definicion_speaker)

    success_rate /= float(N)
    return inventary, success_rate

def counts(inventary):
    N_w = 0
    differents = []
    for objects in inventary:
        for defs in objects:
            N_w += 1
            if defs not in differents:
                differents.append(defs)
    N_d = len(differents)
    return N_w, N_d

def simulation(N, macrosteps):
    #neighs = extract_allwithall(N) # for complete graph
    #neighs = extract_neigh_square(N) # for 2D lattice
    p = 0.08
    neighs = extract_small_world(N,4,p) # small world
    #neighs = extract_scalefreeBA(N,2) #scalefree barabasi-albert
    inventary = [[] for i in range(N)]

    t = 0
    N_w, N_d = counts(inventary)
    total_words = [N_w]
    different_words = [N_d]
    successes = [0]

    for i in range(macrosteps):
        t += 1
        #print("t=%i ..." % t)
        inventary, success_rate = step(N, neighs, inventary)
        successes.append(success_rate)
        N_w, N_d = counts(inventary)
        total_words.append(N_w)
        different_words.append(N_d)
        if t%1000 == 0:
            print("t=%i"%t)

    return total_words, different_words, successes

def simulation_social_zealots(macrosteps): 
    N, zealots, neighs = extract_social_zealots()
    inventary = [[] for i in range(N)]

    for i in zealots:
        inventary[i].append(1)

    t = 0
    N_w, N_d = counts(inventary)
    total_words = [N_w]
    different_words = [N_d]
    successes = [0]

    for i in range(macrosteps):
        t += 1
        inventary, success_rate = step_zealots(N, zealots, neighs, inventary)
        successes.append(success_rate)
        N_w, N_d = counts(inventary)
        total_words.append(N_w)
        different_words.append(N_d)
        if t%100 == 0:
            print("t=%i"%t)

    return total_words, different_words, successes

def simulation_social(macrosteps): 
    N, neighs = extract_social()
    inventary = [[] for i in range(N)]

    t = 0
    N_w, N_d = counts(inventary)
    total_words = [N_w]
    different_words = [N_d]
    successes = [0]

    for i in range(macrosteps):
        t += 1
        inventary, success_rate = step(N, neighs, inventary)
        successes.append(success_rate)
        N_w, N_d = counts(inventary)
        total_words.append(N_w)
        different_words.append(N_d)
        if t%1000 == 0:
            print("t=%i"%t)

    return total_words, different_words, successes

def simulation_small(N, macrosteps,p):
    neighs = extract_small_world(N,4,p) # small world
    inventary = [[] for i in range(N)]

    t = 0
    N_w, N_d = counts(inventary)
    tiempo = []
    total_words = []
    different_words = []
    successes = []

    for i in range(macrosteps):
        t += 1
        inventary, success_rate = step(N, neighs, inventary)
        if np.log10(t) in [0,1,2,3,4,5]:
            cuentas = 0
            paso = t
            siguiente = 0
        if cuentas == siguiente:
            #print("   vamos por tiempo %i"%t)
            tiempo.append(t)
            N_w, N_d = counts(inventary)
            total_words.append(N_w)
            different_words.append(N_d)
            successes.append(success_rate)
            siguiente += paso
        cuentas += 1

    return tiempo,total_words, different_words, successes

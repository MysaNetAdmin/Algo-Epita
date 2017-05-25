from GraphMat import GraphMat
from Graph import Graph
from AlgoPy import queue
from AlgoPy.queue import Queue
from AlgoPy.stack import Stack
import graphviz as gv

def addEdge(G, src, dst):
    if src < 0 or src >= G.order:
        raise Exception("Invalid src")
    if dst < 0 or dst >= G.order:
        raise Exception("Invalid dst")
    G.adj[src][dst] += 1
    if not G.directed and src != dst:
        G.adj[dst][src] += 1
    return G

def addEdgeAdj(G, src, dst):
    if src < 0 or src >= G.order:
        raise Exception("Invalid src")
    if dst < 0 or dst >= G.order:
        raise Exception("Invalid dst")
    G.adjLists[src].append(dst)
    if not G.directed and src != dst:
        G.adj[dst].append(src)

def toDot(G):
    file = open("graphMat.dot", 'w')
    if G == None:
        return ' '
    if G.directed:
        s = "digraph G{\n"
        sep = " -> "
    else:
        s = "graph G{\n"
        sep = " -- "
    for i in range (G.order):
        jMax = G.order if G.directed else i + 1
        for j in range (jMax):
            for k in range(G.adj[i][j]):
                s += ' ' + str(i) + sep + str(j) + '\n'
    s += "}\n"
    file.write(s)
    file.close
    return s

def toDotAdj(G):
    if G == None:
        return ' '
    if G.directed:
        s = "digraph G{\n"
        sep = " -> "
    else:
        s = "graph G{\n"
        sep = " -- "
    for i in range (G.order):
        jMax = G.order if G.directed else i + 1
        for j in range (G.adjLists[i]):
            if j < jMax:
                s += ' ' + str(i) + sep + str(j) + '\n'
    s += "}\n"
    return s

def fromGRAMat(filename):
    file = open(filename, 'r')
    directed = (0 != int(file.readline().strip()))
    order = int(file.readline().strip())
    G = GraphMat(oder, directed)
    for line in file.readline:
        line = line.strip().split()
        addEdge(G, int(line[0]), int(line[1]))
    file.close()
    return G

def fromGRA(filename):
    file = open(filename, 'r')
    directed = (0 != int(file.readline().strip()))
    order = int(file.readline().strip())
    G = Graph(oder, directed)
    for line in file.readline:
        line = line.strip().split()
        addEdge(G, int(line[0]), int(line[1]))
    file.close()
    return G

def __bfs(G, src, M):
    Q = Queue()
    Q = queue.enqueue(src, Q)
    M[src] = -1
    while not queue.isEmpty(Q):
        src = queue.dequeue(Q)
        for dst in range (G.order):
            if G.adj[src][dst] > 0 and M[dst] == None:
                Q = queue.enqueue(dst, Q)
                M[dst] = src

def bfs(G, src):
    M = [ None ] * G.order
    __bfs(G, src,  M)
    for som in range(G.order):
        if M[som] == None:
            __bfs(G, som, M)
    return M

def __bfsAdj(G, src, M):
    Q = Queue()
    Q = queue.enqueue(G, Q)
    M[src] = -1
    while not queue.isEmpty(Q):
        src = queue.dequeue(Q)
        for dst in G.adjLists[src]:
            if M[dst] == None:
                Q = queue.enqueue(dst, Q)
                M[dst] = src

def bfsAdj(G, src):
    M = [ None ] * G.order
    __bfsAdj(G, src,  M)
    for som in range(G.order):
        if M[som] == None:
            __bfsAdj(G, som, M)
    return M

def __dfsMat(G, src, M):
    for dst in range(G.order):
        if G.adj[src][dst] > 0:
            if M[dst] == None:
                M[dst] = src
                print('edge', src, '->', dst)
                __dfsMat(G, dst, M)
            elif M[src] != dst:
                print('back edge', src, '->', dst)

def dfsMat(G, src):
    M = [ None ] * G.order
    M[src] = -1
    __dfsMat(G, src, M)
    for som in range(G.order):
        if M[som] == None:
            M[som] = - 1
            __dfsMat(G, som, M)
    return M

def __dfsAdj(G, src, M, cpt, preff, suff):
    cpt += 1
    pref[src] = cpt
    # Successors
    for dst in ajdLists[src]:
        if M[dst] == None:
            M[dst] = src
            print('edge', src, '->', dst)
            cpt = __dfsAdj(G, dst, M, cpt, preff, suff)
        elif pref[src] < pref[dst]:
            print('forward edge', src, '->', dst)
        elif suff[dst] == None:
            print('back edge', src, '->', dst)
        else:
            print('cross edge', src, '->', dst)
    # Suffix
    cpt += 1
    suff[src] = cpt
    return cpt

def dfsAdj(G, src):
    M = [ None ] * G.order
    preff = [ None ] * G.order
    suff = [ None ] * G.order
    cpt = 0
    M[src] = -1
    cpt = __dfsAdj(G, src, M, cpt, preff, suff)
    for som in range(G.order):
        if M[som] == None:
            M[som] = - 1
            cpt = __dfsAdj(G, som, M, cpt, preff, suff)
    return M

def __isBipartite(G, src, M):
    for dst in range(G.order):
        if G.adj[src][dst] > 0:
            if M[dst] == None:
                M[dst] = 1 - M[src]
                if not __isBipartite(G, dst,  M):
                    return False
            elif M[dst] == M[src]:
                return False
    return True

def isBipartite(G):
    M = [ None ] * G.order
    for src in range(G.order):
        if M[src] == None:
            M[src] = 1
            if not __isBipartite(G, src, M):
                return False
    return True

def isBipartite(G):
    M = [ None ] * G.order
    Q = Queue()
    for src in range(G.order):
        if M[src] == None:
            M[src] = 1
            queue.enqueue(src, Q)
            while not queue.isEmpty(Q):
                src = queue.dequeue(Q)
                for dst in range(G.order):
                    if G.adj[src][dst] > 0:
                        if M[dst] == None:
                            M[dst] = 1 - M[src]
                            queue.enqueue(dst, Q)
                        elif M[dst] == M[src]:
                            return False
    return True

def __isTree(G, src, M):
    for dst in G.adjLists[src]:
        if M[dst] == None:
            M[dst] = src
            if not __isTree(G, dst, M):
                return False
        elif M[src] != dst:
            return False
    return True

def isTree(G):
    M = [ None ] * G.order
    M[0] = - 1
    if not __isTree(G, 0, M):
        return False
    for src in range(1, G.order):
        if M[src] == None:
            return False
    return True

def maxDist1(G, src):
    Q = Queue()
    Q = queue.enqueue(src, Q)
    M = [ None ] * G. order
    M[src] = -1
    cpt, lastSom = 0, 0
    while not queue.isEmpty(Q):
        src = queue.dequeue(Q)
        if src == None:
            if not queue.isEmpty(Q):
                cpt +=1
                queue.enqueue(None, Q)
        else:
            lastSom = src
            for dst in G.adjlists[src]:
                if M[dst] == None:
                    Q = queue.enqueue(adj, Q)
                    dist[dst] = dist[src]-1
    return (cpt, lastSom)

def maxDist(G, src):
    Q = Queue()
    Q = queue.enqueue(src, Q)
    dist = [ None ] * G. order
    dist[src] = 0
    while not queue.isEmpty(Q):
        src = queue.dequeue(Q)
        for dst in G.adjlists[src]:
            if dist[adj] == None:
                Q = queue.enqueue(adj, Q)
                dist[dst] = dist[src]-1
    return (dist[src], src)

def diameter(G):
    d1, s1 = maxDist(G, 0)
    d2, s2 = maxDist(G, s1)
    return d2

def __topoSort(G, src, M, S):
    M[ src ] = True
    for dst in G.adjLists[src]:
        if not M[dst]:
            __topoSort(G, dst, M, S)
    stack.push(src, S)

def topoSort(G):
    M = [ False ] * G.order
    S = Stack()
    __topoSort(G, src,  M)
    for som in range(G.order):
        if M[som] == None:
            __topoSort(G, src,  M)
    L = []
    while not stack.isEmpty(S):
        L.append(stack.pop(S))
    return L

def buildGraph(G, s, n, NG):
    Q = Queue()
    Q = queue.enqueue(s, Q)

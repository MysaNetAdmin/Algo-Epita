from GraphMat import GraphMat
from Graph import Graph
from AlgoPy import queue
from AlgoPy.queue import Queue
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
    if G == None:
        return ' '
    if G.directed:
        s = "diagraph G{\n"
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
    return s

def toDotAdj(G):
    if G == None:
        return ' '
    if G.directed:
        s = "diagraph G{\n"
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

def fromGRA(filename):
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
    G = GraphMat(oder, directed)
    for line in file.readline:
        line = line.strip().split()
        addEdge(G, int(line[0]), int(line[1]))
    file.close()
    return G

def __bfs(G, src, M):
    Q = Queue()
    Q = queue.enqueue(G, Q)
    M[src] = -1
    while not queue.isEmpty(Q):
        src = queue.dequeue(Q)
        for dst in range (G.order):
            if G.adj[src][dst] > 0 and M[dst] == None:
                Q = queue.enqueue(dst, Q)
                M[dst] = src

def bfs(G, src):
    M = [ None] * G.order
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
    M = [ None] * G.order
    __bfs(G, src,  M)
    for som in range(G.order):
        if M[som] == None:
            __bfsAdj(G, som, M)
    return M

G = GraphMat(9, True)
addEdge(G, 0, 1)
addEdge(G, 0, 2)
addEdge(G, 0, 6)
addEdge(G, 1, 3)
addEdge(G, 2, 8)
addEdge(G, 2, 6)
addEdge(G, 3, 6)
addEdge(G, 5, 2)
addEdge(G, 5, 6)
addEdge(G, 6, 3)
addEdge(G, 6, 4)
addEdge(G, 7, 5)
addEdge(G, 7, 6)
addEdge(G, 7, 8)
g1 = toDot(G)

#print(bfs(G, 8))

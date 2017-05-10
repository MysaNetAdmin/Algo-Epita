from GraphMat import GraphMat
from Graph import Graph

def addEdge(G, src, dst):
    if src < 0 or src >= G.order:
        raise Exception("Invalid src")
    if dst < 0 or dst >= G.order:
        raise Exception("Invalid dst")
    G.adj[src][dst] += 1
    if not G.directed and src != dst:
        G.adj[dst][src] += 1
    return G

def addEdge(G, src, dst):
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
        for j in range (G.adjLists[i]):
            if j < jMax:
                s += ' ' + str(i) + sep + str(j) + '\n'
    s += "}\n"
    return s

def fraomGRA(filename):
    file = open(filename, 'r')
    directed = (0 != int(file.readline().strip()))
    order = int(file.readline().strip())
    G = GraphMat(oder, directed)
    for line in file.readline:
        line = line.strip().split()
        addEdge(G, int(line[0]), int(line[1]))
    file.close()
    return G

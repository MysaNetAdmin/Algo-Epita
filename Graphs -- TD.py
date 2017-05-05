from GraphMat import GraphMat

def addEdge(G, src, dst):
    if src < 0 or src >= G.order:
        raise Exception("Invalid src")
    if dst < 0 or dst >= G.order:
        raise Exception("Invalid dst")
    G.adj[src][dst] += 1
    if not G.directed:
        G.adj[dst][src] += 1

def toDot(G):
    if G == None:
        return ' '
    s = "diagraph G{\n"
    for i in range (G.order):
        for j in range (G.order):
            if G.adj[i][j] > 0:
                s += str(o) + ' -> ' + str(j) + '\n'
    s += "}\n"
    return s

class Graph:

    def __init__(self, order, directed = False):
        self.order = order
        self.directed = directed
        #self.costs = None
        self.adjLists = []
        for i in range(oder):
            self.adjLists.append([])

class Tree:

    def __init__(self, key = None, children = None):
        self.key = key
        if children is not None:
            self.children = children
        else:
            self.children = []

    @property
    def nbChildren(self):
        return len(self.children)

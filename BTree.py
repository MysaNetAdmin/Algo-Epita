class BTree:
    degree = None
    
    def __init__(self, keys = None, children = None):
        self.keys = keys if keys else []
        self.children = children if children else []
            
    @property
    def nbKeys(self):
        return len(self.keys)
    
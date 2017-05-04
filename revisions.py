# Build List

import random
random.seed

def buildList(nb, val = None, alea = None):
    if val != None or alea == None:
        return [val] * nb
    else:
        left, right = alea[0], alea[1] - 1
        return [random.randint(left,right)]*nb

# Build Matrix

def buildMatrix(nbL, nbC, val = None, alea = None):
    L = []
    if val != None or alea == None:
        L += [val] * nbC
    else:
        left, right = alea[0], alea[1] - 1
        return [random.randint(left,right)]*nbC
    if nbC <= 0:
        return L
    else:    
        result = []
        while nbL > 0:
            result += L
            nbL -=1

dict = {'Name', 'Zara', 'Age', 'Class', 'First'}
dict.update('lel')
print(dict)
from BTree import BTree

BTree.degree = 2

# To Dot File

def __toDotFile(B, file):
    if B == None:
        return
    b = (B.children != [])
    for i in range(B.nbKeys):
        file.write(str(B.keys[i]) if i == 0 else ' ' + str(B.keys[i]))
        if b:
            file.write('--{')
            __toDotFile(B.children[i], file)
            file.write('}\n')
    if b:
        file.write(str(B.keys[-1]))
        file.write('--{')
        __toDotFile(B.children[-1], file)
        file.write('}\n')

def toDotFile(B, fileName):
    file = open(fileName, 'w')
    file.write("graph{\n")
    __toDotFile(B, file)
    file.write("}\n")
    file.close

# Exercice 1.3 -- Bonus

def __fromList(s, i = 0):
    if i < len(s) and s[i] == '(':
        i += 2
        B = BTree()
        while s[i] != '>':
            key = ""
            while not (s[i] in ',>'): # s[i] != ',' and s[i] != '>'
                key += s[i]
                i += 1
            B.keys.append(int(key))
            if s[i] == ',':
                i += 1
        i += 1 # to pass the '>'
        B.children = []
        while s[i] != ')':
            (C, i) = __fromList(s, i)
            B.children.append(C)
        i += 1
        return (B, i)

def fromList(s, d):
    BTree.degree = d
    (B, i) = __fromList(s)
    return B

B = fromList("(<13, 32, 44>(<3>)(<18, 25>)(<35, 40>)(<46, 49, 50>))", 2)
toDotFile(B, "test.dot")

def __binarySearchPos(L, x, left, right):
    if right <= left:
        return right
    mid = left + (right - left) // 2
    if L[mid] == x:
        return mid
    elif x < L[mid]:
        return __binarySearchPos(L, x, left, mid)
    else:
        return __binarySearchPos(L, x, mid + 1, right)

def binarySearchPos(L, x):
    return __binarySearchPos(L, x, 0, len(L))

# Exercice 2.1 (Min et Max dans un B Tree)

def minBTree(B):
    while B.children != []:
        B.children[0]
    return B.keys[0]

def maxBTree(B):
    while B.children != []:
        B.children[-1]
    return B.keys[-1]

# Exercice 2.2 (Recherche dans un B Arbre)

def __find(B, x):
    pos = binarySearchPos(B.keys, x)
    if pos <= B.nbKeys and B.keys[pos] == x:
        return (B, pos)
    elif B.children != []:
        return __find(B.children[pos], x)
    else:
        return None

def find(B, x):
    if B == None:
        return None
    else:
        return __find(B, x)

# Exercice 2.3 (Insertion B Tree)

def split(B, i):
    mid = BTree.degree - 1
    L = B.children[i]
    R = BTree()
    # Keys
    (L.keys, x, R.keys) = (L.keys[:mid], L.keys[mid], L.keys[mid+1:])
    # Children
    if L.children != []:
        (L.children, R.children) = (L.children[:mid+1], L.children[mid+1:])
    # Root
    B.keys.insert(i, x)
    B.children.insert(i+1, R)

def __insert(x, B):
    i = binarySearchPos(B.keys, x)
    if i < B.nbKeys and B.keys[i] == x:
        return False
    elif B.children == []:
        B.keys.insert(i, x)
        return True
    else:
        if B.children[i].nbKeys == 2 * BTree.degree - 1:
            if B.children[i].keys[BTree.degree - 1] == x:
                return False
            split(B, i)
            if B.keys[i] < x:
                i += 1
        return __insert(x, B.children[i])


def insert(x, B):
    if B == None:
        B = BTree([x])
    else:
        if (2 * BTree.degree - 1 == B.nbKeys):
            R = BTree([], [B])
            split(R, 0)
            B = R
        __insert(x, B)
    return B

# Exercice 2.4 (Suppression B Tree)

def leftRotation(B, i):
    '''
    makes a rotation from child i+1 to child i
    Conditions:
    - the tree B exists
    - its child i exist and its root is not a 2t-node
    - its child i+1 exist and its root is not a t-node
    '''
    L = B.children[i]
    R = B.children[i + 1]
    L.keys.append(B.keys[i])
    B.keys[i] = R.keys.pop(0)
    L.children.append(R.children.pop(0))

def rightRotation(B, i):
    '''
    makes a rotation from child i-1 to child i
    Conditions:
    - the tree B exists
    - its child i exist and its root is not a 2t-node
    - its child i-1 exist and its root is not a t-node
    '''
    L = B.children[i - 1]
    R = B.children[i]
    R.keys.insert(0, B.keys[i - 1])
    B.keys[i - 1] = L.keys.pop()
    if L.children != []:
        R.children.insert(0, L.children.pop())

def merge(B, i):
    '''
    merge B children i and i+1 into child i
    Conditions:
    - the tree b exists and its root is not a t-node
    - children i and i+1 exist and their roots are t-nodes
    '''
    L = B.children[i]
    R = B.children.pop(i + 1)
    L.keys.append(B.keys.pop(i))
    L.keys += R.keys
    if L.children != []:
        L.children += R.children

def __delete(B, x):
    i = binarySearchPos(B.keys, x)
    if B.children != []:
        if i < B.nbKeys and x == B.keys[i]:
            if B.children[i+1].nbKeys > B.children[i].nbKeys:
                B.keys[i] = minBTree(B.children[i+1])
                __delete(B.children[i+1], B.keys[i])
            elif B.children[i].nbKeys > BTree.degree - 1:
                B.keys[i] = maxBTree(B.children[i])
                __delete(B.children[i], B.keys[i])
            else:
                merge(B, i)
                __delete(B.children[i], x)
        else:
            if B.children[i].nbKeys == BTree.degree - 1:
                if i > 0 and B.children[i-1].nbKeys > BTree.degree - 1:
                    rightRotation(B, i)
                elif i < B.nbKeys and B.children[i+1].nbKeys > BTree.degree - 1:
                    leftRotation(B, i)
                else:
                    i = min(i, B.nbKeys - 1)
                    merge(B, i)
            __delete(B.children[i], x)
    else:
        if i < B.nbKeys and x == B.keys[i]:
            B.keys.pop(i)

def delete(B, x):
    if B != None:
        __delete(B, x)
        if B.nbKeys > 0:
            return B
        elif B.children:
            return B.children[0]
    return None

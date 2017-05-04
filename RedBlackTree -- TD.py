from RedBlackTree import RedBlackTree

def height(RBT):
    if RBT == None:
        return 1
    else:
        return RBT.red + height(RBT.left)

def size(RBT):
    if RBT == None:
        return 0
    else:
        return RBT.red + size(RBT.left) + size(RBT.right)

def split(RBT):
    (RBT.left.red, RBT.right.red) = (False, False)
    RBT.red = True
    return RBT

def lr(RBT):
    L = RBT.right
    RBT.left = L.left
    L.left = RBT
    L.red = False
    RBT.red = True
    return RBT

def rr(RBT):
    R = RBT.left
    RBT.left = R.right
    R.right = RBT
    R.red = False
    RBT.red = True
    return RBT

def lrr(RBT):
    RL = RBT.left.right
    RBT.left.right = RL.right
    RL.left = RBT.left
    RL.red = False
    RBT.red = True
    RBT.left = RL.right
    RL.right = RBT
    RBT = RL
    return RBT

def rlr(RBT):
    LR = RBT.right.left
    RBT.right.left = LR.left
    LR.right = RBT.right
    LR.red = False
    RBT.red = True
    RBT.right = LR.left
    LR.left = RBT
    RBT = RL
    return RBT

def __insert(x, RBT):
    if RBT == None:
        return RedBlackTree(x, True), 1
    if RBT.key == x:
        return RBT, 0
    elif x < RBT.key:
        RBT.left, nbRed = __insert(x, RBT.left)
        if RBT.red:
            return RBT, nbRed + 1
        else:
            if abs(nbRed) == 2:
                if RBT.right and RBT.right.red:
                    split(RBT)
                    return RBT, 1
                elif nbRed > 0:
                    RBT = rr(RBT)
                else:
                    RBT = lrr(RBT)
            return RBT, 0
    else:
        RBT.right, nbRed = __insert(x, RBT.right)
        if RBT.red:
            return (RBT, 1 - 3 * nbRed)
        else:
            if abs(nbRed) == 2:
                if RBT.left and RBT.left.red:
                    split(RBT)
                    return RBT, 1
                elif nbRed < 0:
                    RBT = lr(RBT)
                else:
                    RBT = rlr(RBT)
            return RBT, 0

def insert(x, RBT):
    RBT, nbRed = __insert(x, RBT)
    RBT.red = False
    return RBT

RBT = insert(1, None)
RBT = insert(8, RBT)
RBT = insert(42, RBT)

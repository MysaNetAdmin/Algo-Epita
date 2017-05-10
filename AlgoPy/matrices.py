# -*- coding: utf-8 -*-
"""
Matrices: classics
January 2016
@author: Nathalie
"""


#------------------------------------------------------------------------
# 1.1 Displays

def printMatrix(M):
    l = len(M)
    c = len(M[0])
    for i in range(l):
        for j in range(c):
            print(M[i][j], end=' ')
        print()
    
def prettyPrintMatrix(M, d):
    l = len(M)
    c = len(M[0])
    line = ""
    for i in range(c*(d+3)+1):
        line = line + '-'
    for i in range(l):
        print(line)
        for j in range(c):
            s = "| {:" + str(d) + "d}"
            print(s.format(M[i][j]), end=' ')
        print('|')
    print(line)

#------------------------------------------------------------------------
# 1.2 Init

def initMat(l, c, val):
    '''
    Init matrix full of "val"
    '''
    M = []
    for i in range(l):
        M.append([])
        for j in range(c):
            M[i].append(val)
    return M

import random
random.seed()
def makeRandomMatrix(l, c, vMax):
    '''
    Init random matrix, with positive values up to vMax
    '''
    M = []
    for i in range(l):
        L = []
        for j in range(c):
            L.append(random.randint(0, vMax))
        M.append(L)
    return M

#--------------------------------------------------------------------
# load matrix from file

def str2int(L):
    for i in range(len(L)):
        L[i] = int(L[i])
    return L

def loadMatrix(file):
    f = open(file)
    lines = f.readlines()
    f.close()
    M = []
    for line in lines:
        M.append(str2int(line.strip().split(' ')))
    return M
        
#--------------------------------------------------------------------
# 1.3 - 1.4 mathematical operations
# matrices are non-empty!
        
def addMat(A, B):
    (l, c) = (len(A), len(A[0]))
    if (l,c) != (len(B), len(B[0])):
        raise Exception("Matrices have not same dimensions")
    M = initMat(l, c, 0)
    for i in range(l):
        for j in range(c):
            M[i][j] = A[i][j] + B[i][j]
    return M

def multMat(A, B):
    m = len(A)
    n = len(A[0])
    if n != len(B):
        raise Exception("Incompatible dimensions")
    p = len(B[0])
    M = initMat(m, p, 0)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                M[i][j] = M[i][j] + A[i][k] * B[k][j]
    return M



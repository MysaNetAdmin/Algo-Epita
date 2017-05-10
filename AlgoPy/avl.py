# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:12:50 2017
@author: Nathalie
"""

class AVL:
    def __init__(self, key, left, right, bal):
        self.key = key
        self.left = left
        self.right = right
        self.bal = bal
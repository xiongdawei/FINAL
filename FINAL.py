#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:33:03 2019

@author: davidxiong
"""

import numpy as np
# Question 12
array = np.zeros([6,6])
array[0][0]=7
array[2][2]=-3
array[2][4]=9
array[4][2]=-1
array[5][1]=-6
array[5][4]=-5
array[5][5]=1
print(array)

def compress(matrix):
    VALUES = []
    ROWC = []
    COL = []
    counter = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if matrix[i][j]!=0:
                VALUES.append(matrix[i][j])
                COL.append(j)
                counter+=1
        ROWC.append(counter)
    return VALUES, COL, ROWC
print(compress(array))

# Question 10
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()
    
    def show(self):
        print(self.stack)
        
    def size(self):
        return len(self.stack)
    
    def search(self,target):
        size = len(self.stack)
        depth=0
        while len(self.stack)!=0:
            X = self.stack.pop()
            if X == target:
                break
            else:
                depth+=1
        if depth==size:
            return "404 Not Found"
        else:
            return depth
      
Elements = ["Theta","Lambda","Zeta","Epsilon","Delta","Gamma","Mu","Alpha"]
#Elements.reverse()
s = Stack()
for k in Elements:
    s.push(k)
s.show()
print(s.search("Theta"))

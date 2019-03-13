# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:49:33 2019
@author: Yahir F. Rivas
80621641
Instructor: Olac Fuentes
Teaching Assistant: Nath, Anindita
Lab3
MW 1:30 - 2:50
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        
def SumTree(T):
    if T is not None:
        return SumTree(T.left.item) + SumTree(T.right.item)
    return None

def FindDepth(T,k):
    if T is None:
        return -1
    if T.item > k:
        return 1 + FindDepth(T.left)
    if T.item < k:
        return 1 + FindDepth(T.right)

def FindHeight(T):
    if T is None:
        return 0 
    else:
        leftDepth = FindHeight(T.left)
        rightDepth = FindHeight(T.right)
        if(leftDepth > rightDepth):
            return 1 + FindHeight(T.left)
        else:
            return 1 + FindHeight(T.right)
'''    
def DrawTree(ax,p,n,x,y):
    if n>0:
        #changes points of x and y
        ax.plot([p[0],p[0]-x],[p[1],p[1]-y], color='k') #Left branches are graphed
        ax.plot([p[0],p[0]+x],[p[1],p[1]-y], color='k') #Right branches are graphed
        
        DrawTree(ax,[p[0]-x,p[1]-y],n-1,x*.5,y*.9)  #Left side recursive call
        DrawTree(ax,[p[0]+x,p[1]-y],n-1,x*.5,y*.9)  #Right side recursive call
fig, ax = plt.subplots()

T = None
#A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42]
A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
for a in A:
    T = Insert(T,a)

n = FindHeight(T) - 1
DrawTree(ax, [0,0], FindHeight(T), 75, 75)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('binary.png') 
'''    
        
def Search(T,k):
	temp = T 
	while temp is not None: 
		if temp.item > k: #if k is smaller than current element
			temp = temp.left
		elif temp.item < k: #if k is larger than current element
			temp = temp.right
		else: #if current element is equal to k
			return temp 
	return None

            
def balancedTree(A):
    if not A:
        return None
    mid = len(A)//2 #gets middle index of sorted list
    bT = BST(A[mid]) #creates a new tree with the middle element as the root
    bT.left = balancedTree(A[:mid]) #creates left branch with numbers less than root
    bT.right = balancedTree(A[mid+1:]) #creates right branch with numbers greater than root
    return bT

def PrintAtDepth(T,d):
    if T is None: #if tree is empty
        return None
    if d == 0: #if depth was reached
        print(T.item)
    else:
        PrintAtDepth(T.left, d-1) #recursive call for left tree
        PrintAtDepth(T.right,d-1) #recursive call for right tree


def SortedList(T):
	if T is not None: 
		if T.left is None: 
			return [T.item] #returns current elemenet
		if T.right is not None: 
			return SortedList(T.left) + [T.item] + SortedList(T.right) #calls recursion with left node, adds current element and calls right node
		elif T.left is not None: 
			return SortedList(T.left) + [T.item] #calls recursion with left node and adds current element

            
T = None
A = [1,2,3,4,5,6,7,8,9,10,12,15,18]
for a in A:
    T = Insert(T,a)
    
'''Problem 2'''
print(Search(T,8))

'''Problem 3'''
T = balancedTree(A)
space = ' '
InOrderD(T,space)

'''Problem 4'''
T1 = None
T1 = balancedTree(A)
print(SortedList(T1))

'''Problem 5'''
for i in range(FindHeight(T)):
    print("Elements at depth" , i , ": " , end = "", flush = True)
    PrintAtDepth(T,i) 









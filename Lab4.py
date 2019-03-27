# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:16:54 2019

@author: Yahir F. Rivas
80621641
Instructor: Olac Fuentes
Teaching Assistant: Nath, Anindita
Lab2
MW 1:30 - 2:50
"""

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
      
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
#Method1       
def height(T):
    if T.isLeaf: #T is at the last Node
        return 0
    return 1 + height(T.child[0]) #Returns 1 + height of the child

#Method2
def SortedList(T):
    l = [] 
    if T is not None: 
        if T.isLeaf:    
            return T.item #returns leaf elements to the list
        for i in range(len(T.item)): 
            l = l + SortedList(T.child[i]) + [T.item[i]] #adds current elements to the list and recursively calls childs
        l = l + SortedList(T.child[-1]) #adds the last child on the tree 
        return l
    
#Method3
def MinAtDepth(T,d):
    if d==0:
        return T.item[0] #return first element
    if T.isLeaf:
        return -1
    return MinAtDepth(T.child[0], d-1) #calls recursively for leftmost child

#Method4       
def MaxAtDepth(T,d):
    if d==0: 
        return T.item[-1] #returns last element
    if T.isLeaf:
        return -1
    return MaxAtDepth(T.child[-1], d-1) #calls recursively for rightmost child.

#Method5
def NodesAtDepth(T,d):
    if d==0:
        for i in range(0, len(T.child),1):
            return 1     
    return NodesAtDepth(T.child[0], d-1)    
    
#Method 6
def PrintAtDepth(T,d):
    if d==0:
        for i in T.item:
            print(i) #print every element on T.item
    else:
        for i in range(0,len(T.child), 1):
            PrintAtDepth(T.child[i], d-1) #recursively calls all possible childs
#Method 8             
def FullLeaves(T):
	if T.isLeaf: 
		if len(T.item) == T.max_items: #if T is full
			return 1 
	d = 0
	for i in range(len(T.child)): #traverse through childs
		d += FullLeaves(T.child[i])
	return d #return value    
    
    
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')
    
SearchAndPrint(T,60)
SearchAndPrint(T,200)
SearchAndPrint(T,25)
SearchAndPrint(T,20)

print(height(T))
l = SortedList(T)
print(l)
mn = MinAtDepth(T,2)
mx = MaxAtDepth(T,2)
print(mn)
print(mx)
n = NodesAtDepth(T,1)
print(n)
PrintAtDepth(T,1)
f = FullLeaves(T)
print(f)



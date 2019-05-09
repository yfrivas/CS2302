# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:55:30 2019

@author: Yahir F. Rivas
"""
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from collections import deque

def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def countSets(S):
	c = 0
	for i in S:
		if i==-1:
			c+=1
	return c      

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1 

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False
################################################################### Compression Methods
def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
#################################################################
def unionSize(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj: #if different root
        if S[ri] > S[rj]: #if ri is bigger than rj then rj goes to ri
            S[rj] += S[ri]
            S[ri] = rj
            return True
        else:
            S[ri] += S[rj] #if rj is bigger than ri then ri goes to rj
            S[rj] = ri
            return True
    return False

def rWalls(maze, rw):
    if maze < rw -1:
        print("A path from source to destination is not guaranteed to exist")
    elif maze == rw -1:
        print("The is a unique path from source to destination")
    elif maze > rw -1:
        print("There is at least one path from source to destination")
    

def adjacencyList(v, cells):
    #creates list with size cells
    G = [[] for i in range(cells)]
    for i in v:
        G[i[0]].append(i[1]) 
        G[i[1]].append(i[0])
    return G


def breadthFirst(G,v):
    visited = []
    visited = [False for i in range(len(G))]
    prev = []
    prev = [-1 for i in range(len(G))]
    Q = deque([])
    Q.append(v)
    visited[v] = True
    while Q:
        #popleft removes first element in Q
        u = Q.popleft()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.append(t)
    #returns solution of this search            
    return prev

def depthFirst(G,source):
    visited = [False for i in range(len(G))] #Create visited list
    prev = [-1 for i in range(len(G))] #Previous element is set to -1
    Stack = [] 
    Stack.append(source)
    visited[source] = True #mark as visited
    while len(Stack) != 0: #while it is not empty
        s = Stack.pop()
        for t in G[s]:
            if not visited[t]: 
                visited[t] = True #marks as visited
                prev[t] = s #previous node is now the source
                Stack.append(t) 
    return prev
        
def depthFirstR(G,source):
    visited = False
    prev = source
    visited[source] = True
    for t in G[source]: #checks every element in the graph
        if not visited[t]: #if it hasn't been visited
            visited[t] = True #mark as visited
            prev[t] = source #source now becomes previous
            depthFirstR(G,t)      
    return prev
  
#this method prints the path solution given the list      
def printPath(prev,v):
    if prev[v] !=-1:
        printPath(prev,prev[v])
        print(" -> ", end=' ')
    print(v,end=' ') 
    
    
maze_rows = 10  
maze_cols = 15   
    
 
    
cells = maze_rows*maze_cols    
print("The number of cells in the maze is: ", cells)
remWalls = int(input("How many walls do you want to remove?"))
if remWalls < cells - 1:
    print('A path from source to destination is not guaranteed to exist')
if remWalls == cells - 1:
    print(' There is a unique path from source to destination')
if  remWalls > cells - 1:
    print('There is at least one path from source to destination')
    
walls = wall_list(maze_rows,maze_cols)
#draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
newS = DisjointSetForest(maze_rows * maze_cols)
   
while countSets(newS) > 1:
     d = random.randint(0,len(walls)-1) 
     if union(newS, walls[d][0], walls[d][1]): #if they are part of two different sets
         walls.pop(d) 
vertices = []
while remWalls != 0:
    d = random.randint(0,len(walls)-1)
    if union(newS,walls[d][0],walls[d][1]):
        vertices.append(walls[d])
        walls.pop(d)
        remWalls -= 1

G = adjacencyList(vertices, cells)

visited = [False for i in range(len(G))]
prev = [-1 for i in range(len(G))]
print("Adjacency List: ")
print(G)
#print(AdjList(walls, originalWalls, maze))
print()

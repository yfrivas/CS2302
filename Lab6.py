# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:57:48 2019

@author: Yahir F. Rivas
"""

# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
import time

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

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

plt.close("all") 
maze_rows = 10
maze_cols = 15


def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1  

def numSets(S): #return the number of sets
    count = 0
    for i in S:
        if i < 0: #if it is -1 then it is a root so add 1
            count += 1
    return count

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False

plt.close("all")

def countSets(S):
	c = 0
	for i in S:
		if i==-1:
			c+=1
	return c      

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

maze_rows = 10
maze_cols = 15  
walls = wall_list(maze_rows,maze_cols)

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 

S = DisjointSetForest(maze_rows*maze_cols)#use a dsf to create maze
'''
start = time.time()
while countSets(S) > 1: 
    d = random.randint(0,len(walls)-1)
    if union(S,walls[d][0],walls[d][1]): #if they are in different sets
        walls.pop(d) #remove wall
end = time.time() 
rt = end - start
print("The running time for standard union is: ", rt )       

'''
start = time.time()
while countSets(S) > 1:
    d = random.randint(0,len(walls)-1)
    if union_c(S,walls[d][0],walls[d][1]):#if they are in different sets
        walls.pop(d)#remove wall
end = time.time() 
rt = end - start
print("The running time for compression is: ", rt )    
   
    
'''
for i in range(len(walls)//2): #Remove 1/2 of the walls 
    d = random.randint(0,len(walls)-1)
    print('removing wall ',walls[d])
    walls.pop(d)
'''
plt.close("all")

draw_maze(walls,maze_rows,maze_cols) 

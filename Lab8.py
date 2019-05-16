# -*- coding: utf-8 -*-
"""
Created on Fri May 8 14:48:17 2019

@author: Yahir F. Rivas
"""

import random
import numpy as np
from math import *
import time 


def equal(f1, f2,tries=1000,tolerance=0.0001):
    for i in range(tries):
        t = random.uniform(-(math.pi), math.pi)
        y1 = eval(f1)
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True

def compare_trig(f):
    for i in range(len(f)):
        for j in range(1,len(f)):
            if equal(f[i], f[j],tries=1000,tolerance=0.0001):
                print(f[i], " and ", f[j], " are equal")

def subsetsum(S,last,goal):
    if goal == 0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetsum(S,last-1,goal-S[last]) 
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetsum(S,last-1,goal) 
    
def partition(S):
    if sum(S)%2 != 0:
        return False
    goal = sum(S)//2

    return goal

    
    
    
functions = ['sin(t)', 'cos(t)', 'tan(t)', 'sec(t)', '-sin(t)', '-cos(t)',
            '-tan(t)', 'sin(-t)','cos(-t)', 'tan(-t)', 'sin(t)/cos(t)',
            '2*sin(t/2)*cos(t/2)', 'sin(t)*sin(t)','1-cos(t)*cos(t)', '((1-cos(2*t))/2)']

print('Similarities found:')
compare_trig(functions)
print()
S = [2,4,5,9,13]
print('Partition:')
print('Set:' , S)
part = partition(S)
boo, sub1= subsetsum(S,len(S)-1,part)
if part:
    sub2 = []
    print('First subset:',sub1)
    for j in S:
        if j not in sub1:
            sub2.append(j)
    print('Second subset:',sub2)
else:
    print('No partition exists for this set')


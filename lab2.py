# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:39:08 2019

@author: Yahir F. Rivas
80621641
Instructor: Olac Fuentes
Teaching Assistant: Nath, Anindita
Lab2
MW 1:30 - 2:50
"""
from random import random
import time

# List Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)


def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')


class List(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None


def IsEmpty(L):
    return L.head == None


def Append(L, x):
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next


def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line


def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print()


def Remove(L, x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head == None:
        return
    if L.head.item == x:
        if L.head == L.tail:  # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
        # Find x
        temp = L.head
        while temp.next != None and temp.next.item != x:
            temp = temp.next
        if temp.next != None:  # x was found
            if temp.next == L.tail:  # x is the last node
                L.tail = temp
                L.tail.next = None
            else:
                temp.next = temp.next.next


def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()


def ElementAt(L, n):
	if GetLength(L)<n:
		return None
	else:
		temp = L.head
		for i in range(n):
			temp = temp.next
		return temp.item


def GetLength(L):
	temp = L.head
	counter = 0 #counter
	while temp is not None:
		counter = counter + 1
		temp = temp.next
	return counter #return the length

def Preppend(L, n):
    if IsEmpty(L):
        L.head = Node(n)


def Copy(L):
    C = List()
    temp = L.head
    while temp is not None:
        Append(C, temp.item)  # add each item to list C
        temp = temp.next
    return C


def bubbleSort(L):
    change = True
    while change:  # checks for swap in previous iteration
        t = L.head
        change = False
        while t.next is not None:
            if t.item > t.next.item:  # if current element is more than next, then swap
                temp = t.item
                t.item = t.next.item
                t.next.item = temp
                change = True
            t = t.next
    return ElementAt(L, GetLength(L)//2)


def MergeSort(L):
    global count
    len = GetLength(L)  # get the length of L
    if len <= 1:  # if length of list is less or equal to 1 change nothing
        return L
    Left = List()  # create a list for left side
    Right = List()  # create a list for right side
    temp = Copy(L)
    counter = 0
    mid = len // 2
    for i in range(mid):
        Append(Left, temp.head.item)  # Add element to left
        temp.head = temp.head.next
        counter = counter + 1
    while counter < mid:
        Append(Right, temp.head.item)  # Add element to right
        temp.head = temp.head.next
        counter = counter + 1

    LeftList = List()
    LeftList = MergeSort(Left)
    RightList = List()
    RightList = MergeSort(Right)
    MergedList = List()

    while GetLength(MergedList) != len:  # while the merged list doesn't contain all elements
        if IsEmpty(RightList):
            Append(MergedList, LeftList.head.item)
            LeftList.head = LeftList.head.next
        elif IsEmpty(LeftList):
            Append(MergedList, RightList.head.item)
            RightList.head = RightList.head.next
        elif RightList.head.item < LeftList.head.item:  # if RightList's item is smaller than LeftList's item
            count = count + 1
            Append(MergedList, RightList.head.item)  # Add rightlist's item to Sorted list
            RightList.head = RightList.head.next
        else:  # if LeftList's item is smaller than RightList's item
            count = count + 1
            Append(MergedList, LeftList.head.item)  # Add leftlist's item to Sorted list
            LeftList.head = LeftList.head.next
    return MergedList  # return the merged list


def QuickSort(L):
    global count

    RightList = List()  # larger numbers list
    LeftList = List()  # Smaller numbers List
    if GetLength(L) <= 1:  # if length is less or equal to 1 change nothing
        return L
    p = L.head.item  # pivot
    Left = List()  # create a list for left side
    Right = List()  # create a list for right side
    temp = L.head.next
    while temp is not None:
        if temp.item < p:  # if current element is smaller than pivot
            count = count + 1
            Append(Left, temp.item)  # add element to left side
        else:  # if current element is equal or larger than pivot
            count = count + 1
            Append(Right, temp.item)  # add element to right side
        temp = temp.next

    LeftList = QuickSort(Left)

    RightList = QuickSort(Right)

    SortedList = List()
    if IsEmpty(LeftList):  # if pivot is the smallest number
        Append(SortedList, p)  # add pivot to the sorted list
        SortedList.head.next = RightList.head
        SortedList.tail = RightList.tail
        return SortedList
    elif IsEmpty(RightList):  # if pivot is the largest number
        Append(LeftList, p)
        return LeftList
    else:  # pivot in middle
        Append(LeftList, p)
        LeftList.tail.next = RightList.head
        LeftList.tail = RightList.tail
        return LeftList


def QuickSortM(L, n):
    global count
    p = L.head.item
    Left = List()
    Right = List()
    temp = L.head.next
    while temp is not None:
        if temp.item < p:  # if smaller than pivot
            count = count + 1
            Append(Left, temp.item)  # add element on left side
        else:  # else equal or greater than pivot
            count = count + 1
            Append(Right, temp.item)  # add element on right side
        temp = temp.next
    if GetLength(Left) < n:  # median not left of pivot
        count = count + 1
        return QuickSortM(Right, n - GetLength(Left) - 1)  # Search right side for median
    elif GetLength(Left) > n:  # median not right of pivot
        count = count + 1
        return QuickSortM(Left, n)  # search left for median
    else:
        return p

def createList(L, n):
	for i in range(n):
		Append(L, int(random()*101))

def Median(L):
	C = Copy(L)
	print("The median element is: ", bubbleSort(C))
	#print("The median element is: ", ElementAt(MergeSort(C),GetLength(C)//2))
	#print("The median element is: ", ElementAt(QuickSort(C), GetLength(C)//2))
	#print("The median element is: ", QuickSortM(C, GetLength(C)//2))
	return







count = 0
L = List()
createList(L, 10)
#createList(L, 100)
#createList(L, 1000)
Print(L)
bubbleSort(L)
#MergeSort(L)
#QuickSort(L)
#QuickSortM(L, GetLength(L)//2)
Print(L)
Median(L)
    
            

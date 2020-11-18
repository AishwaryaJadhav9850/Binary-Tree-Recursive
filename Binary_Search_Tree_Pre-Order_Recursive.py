# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:53:05 2020

@author: Admin
"""

"""
Binary Search Tree Recursive Depth First Traversal:
    Pre-Order Traversal
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.right=self.left=None
    
def insert(root,data):
    if(root==None):
        root=Node(data)
    elif data < root.data:
        root.left=insert(root.left,data)   
    elif data >= root.data  :  
        root.right=insert(root.right,data) 
    return root
 
def pre_order_DFS(root):
    print(root.data,end=' ')
    if root.left !=None:
        pre_order_DFS(root.left)    
    if root.right !=None:
        pre_order_DFS(root.right)
        
    
n=int(input("Enter the number of elements you want to insert into a Binary Search Tree:- "))
L= [None] * n
root=None
for i in range(n):
    L[i]=int(input("Enter the element:- "))
    root=insert(root,L[i])

print("\nDFS Pre-Order Traversal:")
pre_order_DFS(root)

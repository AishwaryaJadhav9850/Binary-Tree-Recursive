# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:25:41 2020
@author: Admin
"""
"""
Binary Search Tree Recursive Depth First Traversal:
    In-Order Traversal
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
 
def in_order_DFS(root):
    if root.left !=None:
        in_order_DFS(root.left)
    print(root.data,end=' ')
    if root.right !=None:
        in_order_DFS(root.right)

    
    
n=int(input("Enter the number of elements you want to insert into a Binary Search Tree:- "))
L= [None] * n
root=None
for i in range(n):
    L[i]=int(input("Enter the element:- "))
    root=insert(root,L[i])
    
print("\n\nDFS In-Order Traversal:")
in_order_DFS(root)

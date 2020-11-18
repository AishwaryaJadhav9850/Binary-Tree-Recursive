# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:50:38 2020

@author: Admin
"""

"""
Regular Binary Tree Implementation with Recursive Post-Order Depth First Traversal

"""
class Node:
    def __init__(self,data):
        self.data=data
        self.right=self.left=None
    
def insert(root,data):
    if(root==None):        
        root=Node(data)
    print("Enter Left Child for ",root.data,":- ")
    l=input()
    if(l.isdigit()):
        root.left=insert(root.left,int(l))  
    print("Enter Right Child for ",root.data,":- ")
    r=input()
    if(r.isdigit()):
        root.right=insert(root.right,int(r)) 
    return root

             
    
def display(root):   
    if root.left !=None:
        display(root.left)
    if root.right !=None:
        display(root.right)
    print(root.data, end=" ")
  
root=None
i=int(input("Enter data of the node:- "))
root=insert(root,i)
print("Tree Nodes are :")
display(root)

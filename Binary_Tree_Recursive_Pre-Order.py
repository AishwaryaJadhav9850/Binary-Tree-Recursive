# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:19:55 2020

@author: Admin
"""


"""
Regular Binary Tree Implementation with Recursive Pre-Order Depth First Traversal

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
    print(root.data, end=" ")
    if root.left !=None:
        display(root.left)
    if root.right !=None:
        display(root.right)
  
root=None
i=int(input("Enter data of the node:- "))
root=insert(root,i)
print("Tree Nodes are :")
display(root)

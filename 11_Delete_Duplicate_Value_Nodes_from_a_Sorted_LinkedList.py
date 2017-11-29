#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def RemoveDuplicates(head):
    flag = True

    if head == None:
        return head
    elif head.next == None:
        return head
    else:
        node = head
        next_node = node.next

        while flag:
            if node.data == node.next.data:
                node.next = node.next.next

            ##Increment the node to next Node when next node is not the last node and current node data does not match with next node

            if node.next.next != None and node.data != node.next.data:
                node = node.next
            ## When Next Node is NOT the last node
            
            elif node.next.next != None:
                dummy = 0
            ## When next node is the last node and current node and next node have same data and you want to delete the next node by               ## changing current nodes next to NULL and COME OUT OF LOOP By flagging
            
            elif node.data == node.next.data and node.next.next == None:
                node.next = node.next.next
                flag = False
            ##Routine Last Node scenario
            
            else:
                flag = False

        return head



			

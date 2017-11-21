"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if(head==None):
        return(head)
    else:
        node = head
        prev_node = None
        flag = 0
        while(node.next!=None):
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        node.next = prev_node     
    return(node)
  
  
  
  
  
  
  
  


"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    if head is None:
        node = Node()
        node.next = None
        node.data = data
        head = node
    else:
        prev_node = head
        while prev_node.next is not None:
            prev_node = prev_node.next
        node = Node()
        node.next = None
        node.data = data
        prev_node.next = node
    return(head)


  
  
  
  
  
  


"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if head==None:
        head = Node(data, None)
        return(head)
    else:
        node = head
        ctr = position
        if position==0:
            new_node = Node(data, head)
            head = new_node
            return(head)
        else :
            while(node.next != None and ctr >0):
                node = node.next
                ctr = ctr - 1
            new_node = Node(data, node.next)
            node.next = new_node
            return(head)
  
  
  
  
  
  
  
  
  
  

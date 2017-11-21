"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if(head.next == None):
        return None
    else:
        node = head
        ctr = position
        if(position>0):
            while(ctr>0):
                prev_node = node
                node = node.next
                ctr = ctr - 1
            prev_node.next = node.next
        else:
            head = head.next
        return head
        
  
  
  
  
  

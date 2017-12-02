"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if(head == None):
        head = Node(data, None, None)
    else:
        flag = True
        new_node = Node(data, None, None)
        node = head
        while(flag):
            if(node.data > data):                
                new_node.next = node
                if(node != head):
                    new_node.prev = node.prev
                    node.prev.next = new_node
                    node.prev = new_node
                    new_node.next = node                    
                else:
                    new_node.next = node
                    node.prev = new_node
                    head = new_node
                flag = False
            else:
                if(node.next!= None):
                    node = node.next
                else:
                    new_node.prev = node
                    node.next = new_node
                    flag = False
            
    return head    
        
        
  
  
  
  
  
  
  
  
  
  

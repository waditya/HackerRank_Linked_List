#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    
    node = head
    
    #Calculate Number of Nodes in the link List
    
    no_of_nodes = 1
    if(node == None):
        no_of_nodes = 0
    else:
        while(node.next != None):
            no_of_nodes = no_of_nodes + 1
            node = node.next
        
    #Assign node to head node    
    node = head
    if(no_of_nodes == 0):
        return(None)
    else:        
        for i in range(1, no_of_nodes - position, 1):
                node = node.next
        return(node.data)
    
  
  
  
  
  
  
  
  


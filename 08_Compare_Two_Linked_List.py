"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    nodeA = headA
    nodeB = headB
    
    while(nodeA != None and nodeB !=None):
        if(nodeA.data != nodeB.data):
            return(0)
        nodeA = nodeA.next
        nodeB = nodeB.next
        
    if(nodeA == None and nodeB == None):
        return(1)
    else:
        return(0)
    
                
            
            
            
  
  
  
  
  
  
  
  
  
  
  
  
  

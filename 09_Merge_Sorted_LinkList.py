"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    
    #Flag
    
    flag = 1
    
    #Counter
    counter = 0
    
    #NodeCounters
    
    counterA = True
    counterB = True
    
    
    ##Pointer to the Heads
    nodeA = headA
    nodeB = headB
    
    if((headA != None) and (headB == None)):
        return(None)
    elif((headA == None) and (headB != None)):
        return(headB)
    elif((headA != None) and (headB == None)):
        return(headA)
    else:
            ctr = 1
            principal_node = Node(None,None);
            node = principal_node
            
            currNodeA = nodeA
            currNodeB = nodeB
            
            while(counterA or counterB):
                if((currNodeA.data < currNodeB.data) and (counterA)):
                    if(ctr == 1):
                        temp = Node(currNodeA.data, None)
                        principal_node.next = temp
                        node = node.next
                        ctr = ctr + 1
                        if(currNodeA.next != None):
                            currNodeA = currNodeA.next
                        else:
                            counterA = False
                    else:
                        temp = Node(currNodeA.data, None)
                        node.next = temp
                        node = node.next
                        if(currNodeA.next != None):
                            currNodeA = currNodeA.next
                        else:
                            counterA = False
                            
                else:
                    if(ctr == 1):
                        temp = Node(currNodeB.data, None)
                        principal_node.next = temp
                        node = node.next
                        ctr = ctr + 1
                        if(currNodeB.next != None):
                            currNodeB= currNodeB.next
                        else:
                            counterB = False
                            currNodeB.data = currNodeA.data + 1
                    else:
                        temp = Node(currNodeB.data, None)
                        node.next = temp
                        node = node.next
                        if(currNodeB.next != None):
                            currNodeB= currNodeB.next
                        else:
                            counterB = False
                            currNodeB.data = currNodeA.data + 1
    return(principal_node.next)
                    
                
                        
                    
                        
        
                
        
        
        
        
  
  
  
  
  
  
  
  
  

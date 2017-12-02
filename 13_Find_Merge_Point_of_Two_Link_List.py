"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    if(headA == None and headB != None):
        return headB.data
    elif(headA != None and headB == None):
        return headA.data
    else:
        nodeA = headA
        nodeB = headB
        
        flag = True
        while(flag):
            if(nodeA.next == nodeB):
                flag = False
            else:
                if(nodeA.next == None):
                    nodeA = headA
                    nodeB = nodeB.next
                else:
                    nodeA = nodeA.next
        return(nodeB.data)
               
  
  
  
  
  
  
  
  
  

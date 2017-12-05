"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    if(head==None):
        return None
    else:
        flag = True
        node = head
        prev_node = Node(None, None, None)
        
        flag = True
        
        ##Traverse at the last node of Link List
        while(flag):
            if(node.next != None):                
                node = node.next
            else:
                flag = False
        
        ##Reverse the node one-by-one
        ##Assign previous node the value of next node
        ##Assign next node the value of prev_node
        
        flag = True
        flag1 = True
        
        #Assign the previous node
        prev_node = node.prev
        
        while(flag):
            
            if(flag1):
                node.prev = node.next
                node.next = prev_node
                if(node.next != None):
                    prev_node = prev_node.prev
                    node = node.next
                    flag1 = False
                else:
                    flag = False
        return(node)
                
                
                
        
        
  
  
  
  
  
  
  

			

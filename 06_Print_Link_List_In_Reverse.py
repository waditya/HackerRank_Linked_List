"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    if(head == None):
        return None
    else:
        node = head
        arr = []
        while(node.next != None):
            arr.append(node.data)
            #print(node.data)
            node = node.next
        arr.append(node.data)
        for i in range(len(arr)):
            print(arr.pop())
        return None
  
  
  
  
    

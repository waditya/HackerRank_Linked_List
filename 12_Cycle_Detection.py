"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    ## No Cycle [Return FALSE] if head in None
    
    if(head == None):
        return(False)
    ## No Cycle [Return FALSE] if only One Node exists
    
    elif(head.next == None):
        return(False)
    ## More than One node exists
    else:
        node = head
        
        ##Create 'Checker-Node' to test loop with 'Node'
        
        checker_node = node.next
        
        ##Create Flag as TRUE to run the loop as long as Flag is True
        
        flag = True
        
        while(flag):
            ## If checker node is not referencing Node , increment the chker node till it is the last node with whom main node is 
            ## to be verified for cycles OR if main node 'Node' is not reference anywhere , INCREMENT the main node and assign checker             ## node to its next node
            if checker_node.next != node:
                
                ## If Checker Node is not the last Node
                
                if checker_node.next != None:
                    checker_node = checker_node.next
                    
                ## Increment the main node 'Node' when checker node is the last node
                else:
                    node = node.next
                    if node.next != None:
                        checker_node = node.next
                    else:
                        ##Break the loop since all nodes have been verified
                        flag = False
                        break
            else:
                ##Break the MAIN loop since Cycles exist!
                flag = True                
                return(flag)
    


import LinkedList

# Problem description:      
# Solution time complexity: 
# Comments:                 

# Linked List Node inside the LinkedList module is declared as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def AreEqual(left: LinkedList.Node, right: LinkedList.Node) -> bool:
    lnode = left
    rnode = right

    while lnode != None and rnode != None:
        if lnode.val != rnode.val:
            return False
        else:
            lnode = lnode.nxt
            rnode = rnode.nxt

    return lnode == None and rnode == None

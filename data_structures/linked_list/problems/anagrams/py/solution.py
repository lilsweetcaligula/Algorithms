import LinkedList

# Problem description:      Given two strings represented as linked lists, determine 
#                           if they are anagrams of each other.
# Solution time complexity: O(n)
# Comments:                 

# Linked List Node inside the LinkedList module is declared as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def AreAnagrams(left: LinkedList.Node, right: LinkedList.Node) -> bool:
    import collections

    if left == None or right == None:
        return False

    lnode  = left
    rnode  = right
    lookup = collections.Counter()
    
    while lnode != None and rnode != None:
        lookup[lnode.val] += 1
        lnode = lnode.nxt
        rnode = rnode.nxt

    # If either node is not None, means either
    # list is bigger than the other. Thus, they
    # cannot be anagrams of each other.
    if lnode != None or rnode != None:
        return False

    rnode = right

    while rnode != None:
        if lookup[rnode.val] == 0:
            return False
        else:
            lookup[rnode.val] -= 1

    return True

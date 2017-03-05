import LinkedList

# Problem description:      Find the length of a linked list.
# Solution time complexity: O(n)
# Comments:                 

# Linked List Node inside the LinkedList module is declared as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def FindLength(head: LinkedList.Node) -> int:
    node  = head
    count = 0

    while node != None:
        count += 1
        node   = node.nxt

    return count

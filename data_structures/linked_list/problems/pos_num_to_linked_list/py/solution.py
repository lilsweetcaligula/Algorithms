# Problem description:      Convert a number into a linked list of its digits.
# Solution time complexity: O(n)
# Comments:                 Notice that we prepend each subsequent digit node to the destination list's head.
#                           Otherwise the result will be in reverse, i.e. f(123) => 3->2->1.
#

import LinkedList

# Linked List Node inside the LinkedList module is defined as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def ConvertPositiveNumToLinkedList(val: int) -> LinkedList.Node:
    node  = None

    while True:
        dig    = val % 10
        val  //= 10
        prev   = LinkedList.Node(dig, node)
        node   = prev
        
        if val == 0:
            break

    return node

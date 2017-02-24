import LinkedList

# Linked List Node inside the LinkedList module is declared as:
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

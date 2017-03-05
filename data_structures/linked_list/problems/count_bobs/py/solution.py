import LinkedList

# Problem description:      Given a string represented as a linked list of characters, count the occurrence
#                           of a substring "bob" in the original string.
# Solution time complexity: O(Kn), where K = len(src) = len('bob') = 3
# Comments:                 Recursive solution.

# Linked List Node inside the LinkedList module is declared as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def CountBobs(head: LinkedList.Node) -> int:
    if head == None or head.nxt == None:
        return 0
    
    node = head

    for c in 'bob':
        if node == None:
            # The list ended here. Substring "bob" cannot
            # be present fully.
            return 0
        elif node.val != c:
            # Mismatch, move the head pointer one node forward 
            # and recurse.
            return CountBobs(head.nxt)
        else:
            # Match so far, move the node pointer one node forward.
            node = node.nxt
    else:
        # If we got this far, we have found the "bob" substring.
        # Jump over a node starting from the head and recurse. 
        # We could jump to the next one but if we just had "bob" 
        # match, head.nxt will have the value of "o", - and there's 
        # no way we have "bob" with the first letter "o".
        return 1 + CountBobs(head.nxt.nxt)

    return 0

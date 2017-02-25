import LinkedList

# Problem description:      Find a pattern represented as a linked list in a target linked list.
# Solution time complexity: O(n^2)
# Comments:                 A brute force solution w/o any optimizations. Simply traverse a list looking for the pattern.
#                           If the node traversing the "pattern" list ever reaches the end (i.e. pnode == null), it is in
#                           the list. The case where a pnode may be equal to null due to the pattern being null, is ruled
#                           out by a test at the beginning of the function.

# Linked List Node inside the LinkedList module is defined as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def FindPatternInLinkedList(head: LinkedList.Node, pattern: LinkedList.Node) -> int:
    if head == None or pattern == None:
        return -1

    index = 0
    tslow = head
    pnode = pattern

    while tslow != None:
        if tslow.val == pattern.val:
            tfast = tslow
            pnode = pattern

            while tfast != None and pnode != None:
                if tfast.val == pnode.val:
                    tfast = tfast.nxt
                    pnode = pnode.nxt
                else:
                    break
                   
            if pnode == None:
                return index

        tslow  = tslow.nxt
        index += 1

    return -1

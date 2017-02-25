import LinkedList

# Linked List Node inside the LinkedList module is declared as:
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

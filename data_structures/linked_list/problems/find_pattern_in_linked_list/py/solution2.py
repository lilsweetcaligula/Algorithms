import LinkedList

# Problem description:      Find a string pattern represented as a linked list in a target linked list.
# Solution time complexity: O(mn)
# Comments:                 Robin-Karp algorithm.

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

    PRIME_MOD  = 1299827
    PRIME_BASE = 31

    patHash    = 0
    patCount   = 0
    patNode    = pattern

    while patNode != None:
        patHash   = (patHash * PRIME_BASE + ord(patNode.val)) % PRIME_MOD
        patCount += 1
        patNode   = patNode.nxt
        
    patMul   = (PRIME_BASE ** patCount) % PRIME_MOD
    srcHash  = 0
    srcCount = 0
    srcSlow  = head
    srcFast  = head

    while srcFast != None:
        srcHash = (srcHash * PRIME_BASE + ord(srcFast.val)) % PRIME_MOD

        if srcCount >= patCount:
            srcHash = (srcHash - patMul * ord(srcSlow.val)) % PRIME_MOD

            if srcHash < 0:
                srcHash += PRIME_MOD

            srcSlow = srcSlow.nxt

        if srcHash == patHash:
            # Could be a hash collision. Make sure
            # the substrings are indeed equal. Do 
            # a back to back substring comparison.

            srcNode = srcSlow
            patNode = pattern

            while srcNode != None and patNode != None:
                if srcNode.val == patNode.val:
                    srcNode = srcNode.nxt
                    patNode = patNode.nxt
                else:
                    break
            else:                
                if patNode == None:
                    return srcCount - patCount + 1

        srcCount += 1
        srcFast   = srcFast.nxt

    return -1

import LinkedList

# Problem description:      Perform addition of two values, represented as two linked lists of their digits
# Solution time complexity: O(n)
# Comments:                 

# Linked List Node inside the LinkedList module is declared as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def AddTwo(left: LinkedList.Node, right: LinkedList.Node) -> LinkedList.Node:
    def ListReverse(head: LinkedList.Node) -> LinkedList.Node:
        prev = None
        curr = head
        
        while curr != None:
            nxt      = curr.nxt
            curr.nxt = prev
            prev     = curr
            curr     = nxt

        return prev

    dummy     = LinkedList.Node(0)
    dest      = dummy

    left      = ListReverse(left)
    right     = ListReverse(right)

    leftNode  = left
    rightNode = right

    carry     = 0

    while leftNode != None or rightNode != None:
        leftVal  = leftNode.val  if leftNode  else 0
        rightVal = rightNode.val if rightNode else 0

        total    = carry + leftVal + rightVal
        carry    = total // 10
        addVal   = total % 10

        dest.nxt = LinkedList.Node(addVal)
        dest     = dest.nxt

        if leftNode:  leftNode  = leftNode.nxt
        if rightNode: rightNode = rightNode.nxt

    if carry > 0:
        dest.nxt = LinkedList.Node(carry)
        dest     = dest.nxt

    return ListReverse(dummy.nxt)

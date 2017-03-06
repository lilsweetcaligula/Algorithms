import LinkedList

# Problem description:      Given a linked list, find its middle node.
# Solution time complexity: O(n)
# Comments:                 Slow/fast pointer technique.
#                           
#                           i)  0->1->2->3->4->5
#                           ii) 0->1->2->3->4->5
#                               S
#                               F
#
#                           iii) o->S
#                                o->x->F
#
#                            iv) o->o->S
#                                o->x->o->x->F
#
#                             v) o->o->o->S
#                                o->x->o->x->o->x->F
#
#                                M == S
#                               

# Linked List Node inside the LinkedList module is declared as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def FindMiddle(head: LinkedList.Node) -> LinkedList.Node:
    if head == None:
        return None

    slow = head
    fast = head

    while fast != None and fast.nxt != None:
        slow = slow.nxt
        fast = fast.nxt.nxt

    return slow

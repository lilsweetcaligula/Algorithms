import LinkedList

# Problem description:      
# Solution time complexity: 
# Comments:                 

# Linked List Node inside the LinkedList module is declared as:
#
#   class Node:
#       def __init__(self, val, nxt=None):
#           self.val = val
#           self.nxt = nxt
#

def DeleteNAfterMNodes(head: LinkedList.Node, n: int, m: int) -> LinkedList.Node:
    if head == None:
        return None

    slow = head

    while slow != None:
        for _ in range(m - 1):
            if slow == None:
                break
            else:
                slow = slow.nxt

        if slow == None:
            break
        else:
            fast = slow.nxt

            for _ in range(n):
                if fast == None:
                    break
                else:
                    fast = fast.nxt

            slow.nxt = fast
            slow     = slow.nxt

    return head

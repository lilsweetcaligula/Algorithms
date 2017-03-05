import LinkedList

# Problem description:      Given a linked list, values n and m, remove n nodes after ever m nodes 
#                           and return the resulting list.
# Solution time complexity: O(n)
# Comments:                 See the comments in the source code. The tricky part is to realize that
#                           we need to stop the traversal of the m subrange on the (m-1)th node, as
#                           opposed to the mth node, which will incidentally be the first node of
#                           the n subrange. We need this in order to link up the last node in the
#                           current m subrange with the next m subrange.

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
        
        # (m-1)th node will be the last node of the m subrange.
        # (m)th node will be the first node in the n subrange, which
        # is to be deleted.
        #
        # We need to land on the (m-1)th node in order to relink it to
        # the next m subrange.        
        for _ in range(m - 1):
            if slow == None:
                break
            else:
                slow = slow.nxt

        if slow == None:
            # If slow == None, we have reached the end of the list,
            # and there's nothing left to delete...
            break
        else:
            fast = slow.nxt

            for _ in range(n):
                if fast == None:
                    # If fast == None, we have reached the end of the list,
                    # and this is as far as we go for the current subrange.
                    break
                else:
                    fast = fast.nxt

            # Link the last node of the m subrange with the first node of
            # the next m subrange. Move forward.
            slow.nxt = fast
            slow     = slow.nxt

    return head

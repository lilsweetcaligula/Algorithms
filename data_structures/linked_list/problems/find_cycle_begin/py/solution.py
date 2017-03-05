# Problem description:      Given a linked list, return the node where the cycle begins, or if there's no cycle, return null.
# Solution time complexity: O(n)
# Comments:                 Floyd-Warshall algorithm.

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        if head == None:
            return None
            
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            # If slow == fast, we have a cycle.
            # Reset the slow pointer to the head of
            # the list and start incrementing both
            # slow and fast pointers by one.
            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    
                return slow
        
        # No cycle.
        return None

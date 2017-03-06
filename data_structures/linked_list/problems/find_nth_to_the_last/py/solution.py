# Problem description:      Find the nth to last element of a singly linked list. The minimum number 
#                           of nodes in list is n.
# Solution time complexity: O(n)
# Comments:                 

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        if head == None:
            return None
            
        slow = head
        fast = head
        
        for _ in range(n):
            fast = fast.next
            
        while fast != None:
            slow = slow.next
            fast = fast.next
            
        return slow

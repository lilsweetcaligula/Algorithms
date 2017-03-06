# Problem description:      Given a linked list, sort it using insertion sort.
# Solution time complexity: O(n^2)
# Comments:                 Dummy node technique. The isSorted() test is optimization and is not part
#                           of the insertion sort algorithm.

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
    @return: bool, True if empty or for each pair of 
             nodes in the list, n1 and n2:
                n1.val <= n2.val
            else False.
    """
    @staticmethod
    def isSorted(head):
        if head == None:
            return True
            
        cur = head
        nxt = head.next
        
        while nxt != None:
            if cur.val > nxt.val:
                return False
            else:
                cur = cur.next
                nxt = nxt.next
                
        return True
    
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        if head == None:
            return None
        
        if Solution.isSorted(head):
            return head
        
        dummy = ListNode(0)
        node  = head
        
        while node != None:
            temp = node.next
            dest = dummy
            
            while dest.next != None and node.val > dest.next.val:
                dest = dest.next
            
            node.next = dest.next
            dest.next = node
            
            node      = temp
            
        return dummy.next

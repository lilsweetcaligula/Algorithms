# Problem description:      Given two linked lists, return the node where the intersection begins, or if there's 
#                           no intersection, return null.
# Solution time complexity: O(n)
# Comments:                 The solution with a lookup table - extra memory.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        lookup = set()
        nodeA  = headA
        
        while nodeA != None:
            lookup.add(nodeA)
            nodeA = nodeA.next
            
        nodeB = headB
        
        while nodeB != None:
            if nodeB in lookup:
                return nodeB
            else:
                nodeB = nodeB.next
        
        return None

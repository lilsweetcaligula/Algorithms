# Problem description:      Given two linked lists, return the node where the intersection begins, or if there's 
#                           no intersection, return null.
# Solution time complexity: O(n)
# Comments:                 The solution with length offset. This solution makes use of the fact that if distance
#                           to the intersection node from headA is equal to headB, we can simply walk both lists
#                           incrementally until we encounter the intersection node.
#
#                           How do we do this? First, we walk both lists and find their lengths. Then we move the
#                           node of the bigger list as many times as required to make the count of nodes to the
#                           end equal in both lists. Now we can simply traverse both lists at the same time incre-
#                           mentally until we encounter the intersection node.
#
#                               a1->a2
#                                     \
#                                      c1->c2->c3 
#                                     /
#                           b1->b2->b3
#
#
#                           i)
#                                  s
#                             x |------|
#                           |---|
#                               a1->a2
#                                     \
#                                      c1->c2->c3 
#                                     /
#                           b1->b2->b3
#
#                           ii)
#                             x      s
#                           |---||------|
#                                      len1
#                               |----------------|
#                               a1->a2->c1->c2->c3
#                           b1->b2->b3->c1->c2->c3
#                            |-------------------|
#                                     len2
#
#                           x = abs(len1 - len2)
#                           
#                           iii) 
#                               a1->a2                        o->a2
#                                     \                            \
#                                      c1->c2->c3                   c1->c2->c3 
#                                     /                            /
#                               b2->b3                        o->b3
#
#                               o->o
#                                   \
#                                    c1 <-- intersection node
#                                   /
#                               o->o
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    @staticmethod
    def computeLinkedListLength(head):
        count = 0
        node  = head
        
        while node != None:
            count += 1
            node   = node.next
            
        return count
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA == None or headB == None:
            return None
        
        lengthA = Solution.computeLinkedListLength(headA)
        lengthB = Solution.computeLinkedListLength(headB)
        
        nodeA   = headA
        nodeB   = headB
        
        countA  = lengthA
        countB  = lengthB
        
        while countA > countB:
            countA -= 1
            nodeA   = nodeA.next
        
        while countB > countA:
            countB -= 1
            nodeB   = nodeB.next
            
        while nodeA != None and nodeB != None:
            if nodeA == nodeB:
                return nodeA
            else:
                nodeA = nodeA.next
                nodeB = nodeB.next
                
        return None

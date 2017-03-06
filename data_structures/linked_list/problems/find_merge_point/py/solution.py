# Problem description:      Given two linked list, return the node where the intersection begins, or if there's 
#                           no intersection, return null.
# Solution time complexity: O(n)
# Comments:                 The solution with two stacks - extra memory.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    @staticmethod
    def linkedListToArray(head):
        result = []
        node   = head
        
        while node != None:
            result.append(node)
            node = node.next
            
        return result
    
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        
        if headA == None or headB == None:
            return None
        
        stackA = Solution.linkedListToArray(headA)
        stackB = Solution.linkedListToArray(headB)
        
        if stackA[-1] != stackB[-1]:
            return None
        
        while len(stackA) > 0 and len(stackB) > 0:
            if stackA[-1] == stackB[-1]:
                stackA.pop()
                stackB.pop()
            else:
                return stackA.pop().next
                
        if len(stackA) > 0:
            return stackA.pop().next
            
        if len(stackB) > 0:
            return stackB.pop().next
            
        return headA
        

# Problem description:      Implement an algorithm to delete a node in the middle of a singly linked 
#                           list, given only access to that node.
# Solution time complexity: O(1)
# Comments:  

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        if node == None or node.next == None:
            return
        
        node.val  = node.next.val
        node.next = node.next.next
        

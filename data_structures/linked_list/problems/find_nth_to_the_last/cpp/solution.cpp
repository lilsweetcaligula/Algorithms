/*
 * Problem description:      Find the nth to last element of a singly linked list.
 *                           The minimum number of nodes in list is n.
 * Solution time complexity: O(n)
 * Comments:                 
 *                           i)  0->1->2->3->4->5
 *                               |-----|
 *                                  n=2
 *                                  |-----|
 *                                     |-----|
 *                                        |-----|
 *                                        ^
 *                                  nth to the last
 */

/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param head: The first node of linked list.
     * @param n: An integer.
     * @return: Nth to last node of a singly linked list. 
     */
    ListNode *nthToLast(ListNode *head, int n) 
    {
        if (head == nullptr) {
            return nullptr;
        }
        
        auto slow = head;
        auto fast = head;
        
        for (auto i = n; i > 0; --i) {
            fast = fast->next;
        }
        
        while (fast != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }
        
        return slow;
    }
};

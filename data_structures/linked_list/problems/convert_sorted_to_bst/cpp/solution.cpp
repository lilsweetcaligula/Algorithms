/*
 * Problem description:      Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
 * Solution time complexity: O(n log n)
 * Comments:                 Given solution is non-destructive to the list it's called on.
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
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param head: The first node of linked list.
     * @return: a tree node
     */
    TreeNode *sortedListToBST(ListNode *head)
    {
        return sortedListToBST(head, nullptr);
    }
    
private:
    /**
     * @param head: The first node of linked list.
     * @param end:  The end node (exclusive) or a nullptr.
     * @return: a tree node which is the middle node of the list.
     */
    ListNode *findMiddle(ListNode *head, ListNode *end)
    {
        if (head == nullptr || head == end) {
            return nullptr;
        }
        
        auto slow = head;
        auto fast = head;
        
        /* The test for fast or fast->next being a nullptr
         * is currently redundant. However, we keep it here
         * for safety - in case the function is called on
         * two nodes belonging to different lists.
         */
    
        while ((fast != nullptr && fast->next != nullptr)
            && (fast != end     && fast->next != end))
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }

    /**
     * @param head: The first node of linked list.
     * @param end:  The end node (exclusive) or a nullptr.
     * @return: a tree node
     */
    TreeNode *sortedListToBST(ListNode *head, ListNode *end) 
    {
        if (head == nullptr || head == end) {
            return nullptr;
        }
        
        auto mid    = findMiddle(head, end);
        
        auto root   = new TreeNode{ mid->val };
        root->left  = sortedListToBST(head, mid);
        root->right = sortedListToBST(mid->next, end);
        
        return root;
    }
};

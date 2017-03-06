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
     * @return: The head of linked list.
     */
    ListNode *insertionSortList(ListNode *head) 
    {
        auto dummy = ListNode{ 0 };
        auto node  = head;
        
        while (node != nullptr) 
        {
            auto next = node->next;
            auto dest = &dummy;
            
            while (dest->next != nullptr && node->val > dest->next->val) {
                dest = dest->next;
            }
            
            node->next = dest->next;
            dest->next = node;
            
            node       = next;
        }
        
        return dummy.next;
    }
};

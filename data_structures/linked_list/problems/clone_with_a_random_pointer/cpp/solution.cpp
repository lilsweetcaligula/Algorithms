/**
 * Problem description:      Make a deep copy of a list, containing nodes with a random pointer to any other node in the list or null.
 * Solution time complexity: O(n)
 * Comments: 
 */

/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    RandomListNode *copyRandomList(RandomListNode *head) 
    {
        if (head == nullptr) {
            return nullptr;
        }
        
        /*
         * Traverse the list, make a deep copy of each node, but
         * do not copy the random pointer yet. Jam the copy of
         * each node in-between the current node and its next
         * node. We need this to ensure an O(1) access to each
         * node's copy.
         */
        
        auto curr = head;
                
        while (curr != nullptr) 
        {
            auto copy  = new RandomListNode{ curr->label };
            
            copy->next = curr->next;
            curr->next = copy;
            
            curr       = curr->next->next;
        }
        
        /*
         * Now that we have an O(1) access to each node's copy,
         * we can set up the random nodes correctly. The copy
         * of the random node will be its next node, thus:
         *
         *  currCopy->random == curr->random->next
         *
         * The random node might be a null, so we need to check
         * for that. If it's indeed null, we leave a null in
         * the copied node.
         */
        
        curr = head;
        
        while (curr != nullptr) 
        {
            auto copy    = curr->next;
            copy->random = curr->random ? curr->random->next : nullptr;
            curr         = curr->next->next;
        }
        
        /*
         * At this point we can split the cloned list from the
         * original one. Don't worry about the unchecked
         * curr->next->next part. curr->next will never be null,
         * since, at this point, the full list's length is 2*N.
         *
         * This is because we made a copy of each node, so the
         * list's length is now twice its size.
         *
         */
        
        auto dummy = RandomListNode{ 0 };
        auto dest  = &dummy;
        curr       = head;
        
        while (curr != nullptr) 
        {
            auto copy  = curr->next;
            
            curr->next = curr->next->next;
            curr       = curr->next;
            
            dest->next = copy;
            dest       = dest->next;
        }
        
        return dummy.next;
    }
};

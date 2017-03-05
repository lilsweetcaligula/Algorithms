/*
 * Problem description:      Given a singly linked list, determine whether it has a cycle.
 * Solution time complexity: O(n)
 * Comments:                 Tortoise/Hare algorithm. slow/fast pointer technique.
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(const struct ListNode *head) 
{
    if (head == NULL) {
        return NULL;   
    }
    
    const struct ListNode *slow = head,
                          *fast = head;
                    
    while (fast != NULL && fast->next != NULL) 
    {
        slow = slow->next;
        fast = fast->next->next;
        
        if (slow == fast) return 1;
    }
    
    return 0;
}

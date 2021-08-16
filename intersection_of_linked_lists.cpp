/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        set<ListNode*> nodeSet;
        
        while ( headA)
        {
            nodeSet.insert(headA);
            headA = headA->next;
        }
        while(headB)
        {
            if(nodeSet.find(headB)!=nodeSet.end())
            {
                return headB;
            }
            headB = headB->next;
        }

            return NULL;
        
        
        
    }
};
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        
        ListNode dummy;
        ListNode* prevK = &dummy;
        
        ListNode* curr = head;
        
        while(curr != NULL) {
            ListNode* firstNode = curr;
            ListNode* kNode = getKthNode(curr, k);
            if ((kNode) == NULL) {
                prevK->next = curr;
                break;
            }
            ListNode* k1Node = kNode->next;
            ListNode* prev = NULL;
            while (curr != k1Node) {
                ListNode* nxt = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nxt;
            }
            prevK->next = prev;
            prevK = firstNode;
            curr = k1Node;
            
        }
        
        return dummy.next;
    }
private:
    ListNode* getKthNode(ListNode* start, int k) {
        ListNode* temp = start;
        while (k > 1 && temp != NULL) {
            temp = temp->next;
            k--;
        }
        
        return temp;
    }
};
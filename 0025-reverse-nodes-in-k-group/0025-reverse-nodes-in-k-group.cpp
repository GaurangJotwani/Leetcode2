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
            ListNode* kPlus1Node = kNode->next;
            ListNode* prev = NULL;
            while (curr != kPlus1Node) {
                ListNode* nxt = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nxt;
            }
            prevK->next = prev;
            prevK = firstNode;
            curr = kPlus1Node;
        }
        return dummy.next;
    }
    ListNode* getKthNode(ListNode* start, int k) {
        ListNode* tmp = start;
        while (k > 1 && tmp != NULL) {
            tmp = tmp->next;
            k--;
        }
        return tmp;
    }
};
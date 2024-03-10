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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) return NULL;
        if (lists.size() == 1) return lists[0];
        return merge(lists, 0, lists.size() - 1);
    }
private:
    ListNode* merge(vector<ListNode*>& lists, int start, int end) {
        if (start == end) return lists[start];
        cout << start << " " << end << "\n";
        int mid = ((start + end) / 2) - 1;
        ListNode* h1;
        ListNode* h2;
        if (end - start != 1) {
            h1 = merge(lists, start, mid);
            h2 = merge(lists, mid + 1, end);
        } else {
            h1 = lists[start];
            h2 = lists[end];
        }
        
        ListNode dummy;
        ListNode* curr = &dummy;
        while (h1 != NULL && h2 != NULL) {
            if (h1->val <= h2->val) {
                curr->next = h1;
                curr = curr->next;
                h1 = h1->next;
            } else {
                curr->next = h2;
                curr = curr->next;
                h2 = h2->next;
            }
        }
        
        if (h1 != NULL) {
            curr->next = h1;
        } else if (h2 != NULL) {
            curr->next = h2;
        }
        
        return dummy.next;
        
    }
};
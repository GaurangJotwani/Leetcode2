class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        vector<int> ans;
        for (int i = digits.size() - 1; i >= 0; i--) {
            int sm = carry + digits[i];
            carry = sm / 10;
            ans.push_back(sm % 10);
        }
        if (carry > 0) ans.push_back(carry);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
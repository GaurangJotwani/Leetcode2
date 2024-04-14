class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int ans = 0;
    for(int i = 31; i >= 0 ; i--){
        int pow = 1LL<<i;
        int bitL = (left&pow) > 0, bitR = (right&pow) > 0;
        if(bitL == bitR){
            ans += bitL*pow;
        }else{
            break;
        }
    }
    return ans;
}
};
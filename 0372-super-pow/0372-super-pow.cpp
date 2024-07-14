#define ll long long


class Solution {
public:
    ll M = 1337;
    
    ll mod(ll x) {
        return ((x % M + M)%M);
    }

    ll mul(ll a, ll b) {
        return mod(mod(a) * mod(b));
    }

    int superPow(int a, vector<int>& b) {
        vector<ll> val(11, 1);
        for (int i = 1; i < val.size(); i++) {
            val[i] = mul((ll)a, val[i - 1]);
        }
        ll val10 = val[val.size()-1];
        vector<ll> pow10(2001, 1);
        pow10[0] = a;
        pow10[1] = val10;
        for (int i = 2; i < pow10.size(); i++) {
            for (int j = 0; j < 10; j++) {
                pow10[i] = mul(pow10[i], pow10[i - 1]);
            }
        }

        ll ans = 1;
        int backCount = 0;

        for (int i = b.size() - 1; i >= 0; i--) {
            for (int j = 0; j < b[i]; j++) {
                ans = mul(ans, pow10[backCount]);
            }
            backCount++;
        }

        return ans;
    }
};
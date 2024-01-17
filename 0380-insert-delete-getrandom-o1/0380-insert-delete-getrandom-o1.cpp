class RandomizedSet {
public:
    unordered_map<int, int> mp;
    vector<int> lst;
    
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (mp.find(val) != mp.end()) return false;
        lst.push_back(val);
        mp[val] = lst.size() - 1;
        return true;
    }
    
    bool remove(int val) {
        if (mp.find(val) == mp.end()) return false;
        int idx = mp[val];
        int cLast = lst[lst.size() - 1];
        lst[idx] = cLast;
        mp[cLast] = idx;
        lst.pop_back();
        mp.erase(val);
        return true;
    }
    
    int getRandom() {
        int randomIndex = rand() % lst.size();
        int randomValue = lst[randomIndex];
        return randomValue;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> is_there;
        bool result = false;
        for (int i : nums) {
            if (!is_there[i]) {
                is_there[i] = true;
            } else {
                result = true;
                break;
            }
        }
        return result;
    }
};
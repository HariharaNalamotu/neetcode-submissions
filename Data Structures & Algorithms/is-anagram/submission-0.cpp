class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_breakdown;
        unordered_map<char, int> t_breakdown;
        if (s.size() != t.size()) {
            return false;
        }
        for (char i : s) {
            s_breakdown[i]++;
        }
        for (char j : t) {
            t_breakdown[j]++;
        }
        for (char i : s) {
            if (s_breakdown[i] != t_breakdown[i]) {
                return false;
            }
        }
        for (char j : t) {
            if (s_breakdown[j] != t_breakdown[j]) {
                return false;
            }
        }
        return true;
    }
};

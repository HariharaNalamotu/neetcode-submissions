class Solution {
public:
    int characterReplacement(string s, int k) {
        if (s.size() < k+1) {
            return s.size();
        }
        int max = k + 1;
        int left = 0;
        int right = 1;
        unordered_map<char, int> lettercount;
        lettercount[s[left]]++;

        while (right <= s.size() && left < s.size()) {
            int maxcount = 0;
            for (auto a : lettercount) {
                if (a.second > maxcount) {
                    maxcount = a.second;
                }
            }
            if (right-left-maxcount <= k && right-left > max) {
                max = right-left;
                right++;
                lettercount[s[right-1]]++;
            } else if (right-left-maxcount <= k) {
                right++;
                lettercount[s[right-1]]++;
            } else if (right-left-maxcount > k) {
                left++;
                lettercount[s[left-1]]--;
            }
        }

        return max;
    }
};

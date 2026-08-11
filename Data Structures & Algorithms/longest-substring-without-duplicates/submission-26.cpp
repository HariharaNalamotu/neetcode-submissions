class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s == "") {
            return 0;
        }
        vector<char> character;
        for (char i : s) {
            character.push_back(i);
        }
        if (character.size() == 1) {
            return 1;
        }
        int l = 0;
        int r = 1;
        int maxLength = 0;
        unordered_map<char, int> letterpos;
        unordered_map<char, int> letternum;
        letterpos[character[l]] = l;
        letternum[character[l]]++;
        while (r < character.size()) {
            if (letternum[character[r]]>0) {
                for (int i = l; i < letterpos[character[r]]; i++) {
                    letterpos[character[i]] = 0;
                    letternum[character[i]]--;
                }
                l = letterpos[character[r]] + 1;
                letterpos[character[r]] = r;
            } else {
                letterpos[character[r]] = r;
                letternum[character[r]]++;
            }
            if (r-l+1>maxLength) {
                maxLength = r-l+1;
            }
            r++;
        }
        return maxLength;
    }
};
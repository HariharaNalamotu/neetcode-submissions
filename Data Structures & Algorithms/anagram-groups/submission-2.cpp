class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> grouped_anagrams;
        unordered_map<string, vector<string>> anagrams;
        
        for (string s : strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            anagrams[sortedS].push_back(s);
        }
        for (auto& anagram : anagrams) {
            grouped_anagrams.push_back(anagram.second);
        }
        return grouped_anagrams;
    }
};

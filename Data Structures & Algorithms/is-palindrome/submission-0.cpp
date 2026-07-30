class Solution {
public:
    bool isPalindrome(string s) {
        string sArray;
        for (char c : s) {
            if (isalnum(c)) {
                sArray += tolower(c);
            }
        }
        cout << sArray;
        int mid = sArray.size()/2;
        for (int i = 0; i < mid; i++) {
            if (sArray[i] != sArray[sArray.size()-1-i]) {
                cout << sArray[i] << " " << sArray[sArray.size()-1-i];
                return false;
            }
        }
        return true;
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = numbers.size()-1; j>i; j--) {
                if (numbers[i] + numbers[j] < target) {
                    break;
                } else if (numbers[i] + numbers[j] == target) {
                    return {i+1, j+1};
                }
            }
        }
    }
};

class Solution {
public:
    int maxArea(vector<int>& heights) {
        int height1 = heights[0];
        int height2 = heights[heights.size()-1];
        int maxpos1 = 0;
        int maxpos2 = heights.size()-1;
        int curpos1 = 0;
        int curpos2 = heights.size()-1;
        int currentLargestArea = min(height1, height2) * (maxpos2-maxpos1);
        while (curpos1 != curpos2) {
            if (min(heights[curpos1], heights[curpos2]) * (curpos2-curpos1) > currentLargestArea) {
                maxpos1 = curpos1;
                maxpos2 = curpos2;
                height1 = heights[curpos1];
                height2 = heights[curpos2];
                currentLargestArea = min(heights[curpos1], heights[curpos2]) * (curpos2-curpos1);
            }
            if (heights[curpos1] < heights[curpos2]) {
                curpos1++;
            } else {
                curpos2--;
            }
        }

        return currentLargestArea;
    }
};

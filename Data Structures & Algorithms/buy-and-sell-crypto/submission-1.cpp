class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int buy = 0;
        int sell = 1;
        while (sell < prices.size()) {
            if (prices[sell]-prices[buy]>maxProfit) {
                maxProfit = prices[sell]-prices[buy];
            } else if (prices[sell]-prices[buy]<0) {
                buy = sell;
            }
            sell++;
        }
        return maxProfit;
    }
};

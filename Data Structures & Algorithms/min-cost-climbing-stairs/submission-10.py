class Solution:
    cache = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.cache = {}
        return self.recursiveMinCostClimbingStairs(len(cost))

    def recursiveMinCostClimbingStairs(self, step):
        cost = self.cost
        onestepcost = 0
        if step == 0:
            return 0
        elif step == 1:
            return 0
        if str(step - 1) in self.cache.keys():
            onestepcost = self.cache[str(step - 1)]
        else:
            self.cache[str(step - 1)] = self.recursiveMinCostClimbingStairs(step - 1)
            onestepcost = self.cache[str(step - 1)]
        onestepcost = onestepcost + cost[step-1]
        twostepcost = 0
        if str(step - 2) in self.cache.keys():
            twostepcost = self.cache[str(step - 2)]
        else:
            self.cache[str(step - 2)] = self.recursiveMinCostClimbingStairs(step - 2)
            twostepcost = self.cache[str(step - 2)]
        twostepcost = twostepcost + cost[step-2]
        return min(onestepcost, twostepcost)

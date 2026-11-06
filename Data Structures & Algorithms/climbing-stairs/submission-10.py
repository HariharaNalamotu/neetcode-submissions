class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n>0:
            if str(n-1) not in self.cache.keys():
                first = self.climbStairs(n-1)
                self.cache[str(n-1)] = first
            else:
                first = self.cache[str(n-1)]
            if str(n-2) not in self.cache.keys():
                second = self.climbStairs(n-2)
                self.cache[str(n-2)] = second
            else:
                second = self.cache[str(n-2)]
            return first + second
        elif n==0:
            return 1
        else:
            return 0
        
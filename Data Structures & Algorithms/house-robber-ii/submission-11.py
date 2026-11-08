class Solution:
    cache = {}

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        self.nums = nums
        self.cache = {}
        one = self.recursiveRob(len(nums) - 1, True)
        self.cache = {}
        two = self.recursiveRob(len(nums) - 2, False)
        self.cache = {}
        three = self.recursiveRob(len(nums) - 3, False)

        return max(one, two, three)

    def recursiveRob(self, housenum, startAtEnd):
        if housenum == 0:
            if startAtEnd:
                return 0
            return self.nums[0]
        elif housenum == 1:
            return self.nums[1]
        elif housenum < 0:
            return 0

        loottwo = 0
        if housenum - 2 in self.cache:
            loottwo = self.cache[housenum - 2]
        else:
            loottwo = self.recursiveRob(housenum - 2, startAtEnd)
            self.cache[housenum - 2] = loottwo

        lootthree = 0
        if housenum - 3 in self.cache:
            lootthree = self.cache[housenum - 3]
        else:
            lootthree = self.recursiveRob(housenum - 3, startAtEnd)
            self.cache[housenum - 3] = lootthree

        return max(loottwo, lootthree) + self.nums[housenum]

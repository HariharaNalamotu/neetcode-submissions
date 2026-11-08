class Solution:
    cache = {}
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.cache = {}
        return max(self.recursiveRob(len(nums)-1), self.recursiveRob(len(nums)-2))
        # you can start at 0 or 1
        # you can skip one house and rob the next or skip 2 and rob the next

    def recursiveRob(self, housenum):
        nums = self.nums
        if housenum == 0:
            return nums[housenum]
        if housenum == 1:
            return nums[housenum]
        if housenum < 0:
            return 0
        twodownloot = 0
        if housenum-2 in self.cache:
            twodownloot = self.cache[housenum-2]
        else:
            twodownloot = self.recursiveRob(housenum-2)
            self.cache[housenum-2] = twodownloot
        threedownloot = 0
        if housenum-3 in self.cache:
            threedownloot = self.cache[housenum-3]
        else:
            threedownloot = self.recursiveRob(housenum-3)
            self.cache[housenum-3] = threedownloot
        return max(twodownloot, threedownloot) + nums[housenum]
        
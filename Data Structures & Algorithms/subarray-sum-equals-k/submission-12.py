class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = []
        prefixFreq = {0: 1}
        resnum = 0
        for i in range(0, len(nums)):
            try:
                prefixSum.append(prefixSum[i - 1] + nums[i])
            except Exception as e:
                prefixSum.append(nums[i])
            if prefixSum[i] - k in prefixFreq:
                resnum += prefixFreq[prefixSum[i] - k]
            if prefixSum[i] in prefixFreq:
                prefixFreq[prefixSum[i]] += 1
            else:
                prefixFreq[prefixSum[i]] = 1

        return resnum

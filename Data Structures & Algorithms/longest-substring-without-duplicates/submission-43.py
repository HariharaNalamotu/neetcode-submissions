class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        left = 0
        right = 1
        chars = {}
        chars[s[left]] = left
        maxlength = 0

        while right < len(s):
            if s[right] not in chars:
                chars[s[right]] = right
            else:
                left = max(left, chars[s[right]] + 1)
                chars[s[right]] = right
            if right - left + 1 > maxlength:
                maxlength = right - left + 1
            right += 1
        return maxlength

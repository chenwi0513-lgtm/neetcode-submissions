class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                length = 1
                iterator = nums[i] + 1
                while iterator in s:
                    length += 1
                    iterator += 1
                l = max(length, l)
        return l
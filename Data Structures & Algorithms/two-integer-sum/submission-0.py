class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            if nums[i] not in s:
                s[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in s and s[target-nums[i]] != i:
                return sorted([i, s[target-nums[i]]])
        return []
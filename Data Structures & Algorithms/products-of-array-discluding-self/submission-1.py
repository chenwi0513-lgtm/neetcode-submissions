class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        ans = []

        for i in range(len(nums) - 1):
            if len(left) == 0:
                left.append(nums[i])
            else:
                left.append(nums[i] * left[-1])
        
        for i in range(len(nums) - 1, 0, -1):
            if len(right) == 0:
                right.append(nums[i])
            else:
                right.append(nums[i] * right[-1])


        lPointer = 0
        rPointer = len(right) - 1

        for i in range(len(nums)):
            ans.append(right[rPointer] * left[lPointer])
            rPointer -= 1
            lPointer += 1
        return ans
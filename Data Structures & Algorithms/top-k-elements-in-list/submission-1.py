class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = [0] * 2001
        freq = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            lst[nums[i] + 1000] += 1
            freq[lst[nums[i] + 1000]].append(nums[i])
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i]) - 1, -1, -1):
                if len(ans) < k and freq[i][j] not in ans:
                    ans.append(freq[i][j])
        return ans
        
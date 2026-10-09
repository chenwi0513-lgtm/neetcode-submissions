class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = [0] * 2001
        freq = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            lst[nums[i] + 1000] += 1
        for i in range(2001):
            if lst[i] > 0:
                freq[lst[i]].append(i - 1000)
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                    ans.append(freq[i][j])
                    if len(ans) == k:
                        return ans
        return ans
        
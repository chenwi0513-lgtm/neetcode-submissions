class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dct = {}
        for i in range(len(strs)):
            lst = [0] * 26
            for char in strs[i]:
                lst[ord(char) - ord('a')] += 1
            t = tuple(lst)
            if t in dct:
                ans[dct[t]].append(strs[i])
            else:
                dct[t] = len(ans)
                ans.append([strs[i]])
        return ans
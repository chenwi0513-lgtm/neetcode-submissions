class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            s += str(len(strs[i])) + chr(266) + strs[i]
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            end = s.find(chr(266), i)
            num = int(s[i:end])
            ans.append(s[i + len(str(num)) + 1: i + len(str(num)) + num + 1])
            i += len(str(num)) + num + 1
            print(i)
        return ans
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for letter in s:
            arr[ord(letter) - ord('a')] += 1
        
        for letter in t:
            arr[ord(letter) - ord('a')] -= 1
        
        return arr == [0] * 26
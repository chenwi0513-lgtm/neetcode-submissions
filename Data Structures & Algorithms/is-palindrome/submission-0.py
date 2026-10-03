class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ""
        for char in s:
            if char.isalnum():
                cleaned_str += char
        cleaned_str = cleaned_str.lower()
        left = 0 
        right = len(cleaned_str) - 1
        while right > left:
            if cleaned_str[left] != cleaned_str[right]:
                return False
            right -= 1
            left += 1
        return True
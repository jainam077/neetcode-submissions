class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = [char for char in s.lower() if char.isalnum()]
        return palindrome == palindrome[::-1]
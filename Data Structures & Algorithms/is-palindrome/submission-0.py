class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = [char for char in s.lower() if char.isalnum()]
        print(palindrome.reverse(),'\n',palindrome)
        return palindrome == palindrome[::-1]
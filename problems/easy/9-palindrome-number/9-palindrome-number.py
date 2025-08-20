
"""
LeetCode 9. Palindrome Number
Difficulty: easy
URL: https://leetcode.com/problems/palindrome-number/

Решение добавлено: 2025-08-20
"""

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)==str(x)[::-1]


num = 1221
res = isPalindrome(num)
print(res)

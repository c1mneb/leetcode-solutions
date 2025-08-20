
"""
LeetCode 13. Roman to Integer
Difficulty: easy
URL: https://leetcode.com/problems/roman-to-integer/

Решение добавлено: 2025-08-20
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        cur_val = 0
        prev_val = 0 
        for sym in s[::-1]:
            cur_val = roman_values[sym]
            if cur_val < prev_val: result -= cur_val
            else: result += cur_val
            prev_val = cur_val
        return result
                
sol = Solution()
str_input = "LVIII"
print(sol.romanToInt(str_input))


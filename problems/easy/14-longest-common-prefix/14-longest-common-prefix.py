
"""
LeetCode 14. Longest Common Prefix
Difficulty: easy
URL: https://leetcode.com/problems/longest-common-prefix/

Решение добавлено: 2025-08-20
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        prefix = strs[0]
        for s in strs[1::]:
            while(s.find(prefix) != 0):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix


strs = ["flower","flow","floght"]
sol = Solution()
common_str = sol.longestCommonPrefix(strs)
print(common_str)

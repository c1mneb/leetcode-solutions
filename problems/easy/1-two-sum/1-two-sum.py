
"""
LeetCode 1. Two Sum
Difficulty: easy
URL: https://leetcode.com/problems/two-sum/

Решение добавлено: 2025-08-20
"""

def func(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)) :
            print(f'num1 = {nums[i]}, num2 = {nums[j]}')
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [3, 2, 4]
target = 6
print(func(nums, target))


"""
LeetCode: Two Sum

Question:
Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target.

You may assume:
- Each input has exactly one solution.
- You may not use the same element twice.
- You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

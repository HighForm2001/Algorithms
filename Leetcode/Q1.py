"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums, target: int):
        seen = {}
        for index, n in enumerate(nums):
            remainder = target - n
            if remainder in seen:
                return [seen[remainder], index]
            else:
                seen[n] = index

if __name__ == "__main__":
    print(Solution().twoSum([3,2,4],6))
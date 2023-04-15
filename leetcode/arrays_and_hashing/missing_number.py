"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""


class Solution:
    def missing_number(self, nums):
        # Solution 1
        # Time complexity: O(2n)
        # Space complexity: O(n)
        # nums = sorted(nums)
        # n = 0
        # for i in range(0, len(nums)):
        #     if n != nums[i]:
        #         return n
        #     n+=1
        # return n

        # Solution 2 Using Gauss's sum formula from 1 to n: n*(n+1)/2
        # Time complexity: O(n) - because of the sum(nums)
        # Space complexity: O(1)
        # n = len(nums)
        # return n * (n+1) // 2 - sum(nums)

        # Solution 3
        # n = len(nums)
        # return sum(range(n+1)) - sum(nums)

        # Solution 4
        # Time complexity: O(n)
        # Space complexity: O(1)
        x = len(nums)
        for i in range(x):
            x ^= i
            x ^= nums[i]
        return x

nums = [3,0,1]
# nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
print(obj.missing_number(nums))
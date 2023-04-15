"""
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.
"""

class Solution:
    def contains_duplicate(self, nums):
        # Solution 1
        # Time Complexity: O(n), Space Complexity: O(n)
        myset = set()
        for i in nums:
            if i in myset:
                return True
            myset.add(i)
        return False

        # Solution 2
        # Time Complexity: O(n), Space Complexity: O(n)
        # hash_table = {}
        # for i in nums:
        #     if i not in hash_table:
        #         hash_table[i] = 0
        #     else:
        #         return True
        # return False


        # Solution 3 > ~ brute force
        # Time Complexity: O(n Log n), Space Complexity: O(1)
        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if (nums[i] == nums[i-1]): 
        #         return True
        # return False


        # Solution 4 > Pythonic style
        # Time Complexity: O(n), Space Complexity: O(1)
        # return len(nums) != len(set(nums))


        # Sol 5 => this solution will not work on leetcode, it will 
        # cause a runtime error (because of the constraints and given tests)
        # list = []
        # for i in nums:
        #     if i not in list:
        #         list.append(i)
        #     else:
        #         return True
        # return False

        # Sol 6 => same issue on leetcode like on solution 5
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         print(nums[i], nums[j])
        #         print()
        #         if nums[i] == nums[j]:
        #             return True
        # return False 


# nums = [1,2,3,1]
# nums = [1,1,1,3,3,4,3,2,4,2]
nums = [0,4,5,0,3,6]
# nums = [3,3]
obj = Solution()
print(obj.contains_duplicate(nums))
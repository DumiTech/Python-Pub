"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

from collections import defaultdict


class Solution():
    def group_anagrams(self, strs):
        # Solution 1
        # d = {}
        # for word in strs:
        #     key = "".join(sorted(word))

        #     if key in d:
        #         d[key].append(word)
        #     else:
        #         d[key] = [word]
        # return d.values()


        # Solution 2
        # defining a default dictionary with values as a list
        # dictionary = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     dictionary[tuple(count)].append(s)

        # return dictionary.values()


        # Solution 3
        # Time complexity: O(m*nlogn))
        # Space complexity: O(n)
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        return d.values()



strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
obj = Solution()
print(obj.group_anagrams(strs))
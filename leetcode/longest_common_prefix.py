'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''


class LongestCommonPrefix:

    def longestCommonPrefix(self, strs):

        if not strs or len(strs) < 1 or len(strs) >= 200:
            return ""

        shortest = min(strs)

        for i, j in enumerate(shortest):
            for str in strs:
                if str[i] != j:
                    return shortest[:i]
        return shortest     


# strs = ["a", "aa"]
strs = ["flower","flow","flight"]
# strs = ["reflower","flow","flight"]
# strs = ["c","acc","ccc"]
obj = LongestCommonPrefix()
print(obj.longestCommonPrefix(strs))
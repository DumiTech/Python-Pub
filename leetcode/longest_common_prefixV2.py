class LongestCommonPrefix:

    def longestCommonPrefix(self, strs):

        if not strs: return ""
        count = 0

        minimum, maximum= min(strs), max(strs)
        for i in range(len(minimum)):
            if minimum[i] != maximum[i]: break
            else: count+=1

        return minimum[:count]

# strs = ["a", "aa"]
# strs = ["flower","flow","flight"]
# strs = ["reflower","flow","flight"]
strs = ["c","acc","ccc"]
obj = LongestCommonPrefix()
print(obj.longestCommonPrefix(strs))
class Roman2Integer:

    def romanToInt(self, s):

        dict = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }

        num = 0
        for i in range(0, len(s) - 1):
            if (dict[s[i]] < dict[s[i+1]]):
                num -= dict[s[i]]
            else:
                num += dict[s[i]]

        return num + dict[s[-1]]

class Solution:
 
    s = "MCMXCIX"
    obj = Roman2Integer()
    print(obj.romanToInt(s))
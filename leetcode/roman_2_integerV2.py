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

        num, tmp = 0, "I"
        # reversing => starting from the end towards the first taking each element
        for c in s[::-1]:
            num = num - dict[c] if dict[c] < dict[tmp] else num + dict[c]
            print("num = {}, dict[c] = {}, dict[tmp] = {}".format(num, dict[c], dict[tmp]))
            tmp = c

        return num


 
s = "IX"
obj = Roman2Integer()
print(obj.romanToInt(s))
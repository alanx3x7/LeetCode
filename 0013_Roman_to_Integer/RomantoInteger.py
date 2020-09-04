class Solution:

    def romanToInt(self, s: str) -> int:

        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num = 0

        while not s == "":
            first = s[0]
            doub = s[0:2] if len(s) > 1 else ""

            if doub == "IV" or doub == "IX" or doub == "XL" or doub == "XC" or doub == "CD" or doub == "CM":
                val = values[doub[1]] - values[doub[0]]
                num = num + val
                s = s[2:]

            else:
                num = num + values[first]
                s = s[1:]

        return num

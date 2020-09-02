class Solution:

    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        cycle_length = numRows * 2 - 2

        result = ""

        for i in range(numRows):
            for j in range(i, len(s), cycle_length):
                result += s[j]

                if i != 0 and i != numRows - 1 and cycle_length - 2 * i + j < len(s):
                    result += s[cycle_length - 2 * i + j]

        return result

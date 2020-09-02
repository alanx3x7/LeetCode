class Solution:

    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        table = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            table[i][i] = 1
            if i < n - 1 and s[i] == s[i + 1]:
                table[i][i + 1] = True

        for length in range(2, n + 1):
            for i in range(n):
                j = i + length
                if j < n and table[i + 1][j - 1] == 1 and s[i] == s[j]:
                    table[i][j] = 1

        longest = 0
        output = ""
        for i in range(n):
            for j in range(i, n):
                if table[i][j] == 1:
                    is_longest = True if (j - i + 1) > longest else False
                    longest = j - i + 1 if is_longest else longest
                    output = s[i:j + 1] if is_longest else output

        return output


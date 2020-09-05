class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        pref = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for j in range(1, len(strs)):
                if len(strs[j]) < i + 1 or strs[j][i] != char:
                    return pref

            pref = pref + char

        return pref

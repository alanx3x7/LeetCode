class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        last_appearance = {}
        longest_length = 0
        current_start = -1

        for i, char in enumerate(s):
            if char in last_appearance and current_start < last_appearance[char]:
                current_start = last_appearance[char]

            last_appearance[char] = i
            longest_length = max(longest_length, i - current_start)

        return longest_length

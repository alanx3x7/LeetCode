class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def recurse_form_phone(letters, digits):
            if len(digits) == 0:
                combinations.append(letters)

            else:
                for letter in phone[digits[0]]:
                    recurse_form_phone(letters + letter, digits[1:])

        combinations = []
        if digits:
            recurse_form_phone("", digits)
        return combinations

class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for character in s:

            if character in mapping:

                top = stack.pop() if stack else '#'

                if mapping[character] != top:
                    return False

            else:

                stack.append(character)

        return len(stack) == 0

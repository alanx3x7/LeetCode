class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(current, nopen, nclose):
            if len(current) == n * 2:
                possibilities.append(current)
                return

            if nopen < n:
                backtrack(current + "(", nopen + 1, nclose)

            if nclose < nopen:
                backtrack(current + ")", nopen, nclose + 1)

        possibilities = []
        backtrack("", 0, 0)
        return possibilities

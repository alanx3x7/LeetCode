class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed = 0
        while x > reversed:
            number = x % 10
            reversed = reversed * 10 + number
            x = x // 10

        return x == reversed or x == reversed // 10

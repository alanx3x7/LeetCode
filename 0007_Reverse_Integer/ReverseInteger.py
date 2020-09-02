class Solution:

    def reverse(self, x: int) -> int:

        reversed_num = 0
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        while x != 0:
            popped = x % 10
            x = x // 10

            if not is_negative and (
                    reversed_num > (2 ** 31 - 1) // 10 or (reversed_num == (2 ** 31 - 1) // 10 and popped > 7)):
                return 0
            if is_negative and (reversed_num > 2 ** 31 // 10 or (reversed_num == 2 ** 31 // 10 and popped > 8)):
                return 0

            temp = reversed_num * 10 + popped
            reversed_num = temp

        return reversed_num if not is_negative else reversed_num * -1

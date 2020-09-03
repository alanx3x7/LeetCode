class Solution:
    def myAtoi(self, str: str) -> int:

        number = 0
        seen_number = False
        is_negative = 1

        for i in str:

            if not seen_number:
                if ord(i) == 32:
                    continue
                if ord(i) == 45:
                    is_negative = -1
                    seen_number = True
                    continue
                if ord(i) == 43:
                    seen_number = True
                    continue

            if ord(i) < 48 or ord(i) > 57:
                return number

            seen_number = True

            value = ord(i) - 48
            value = value * is_negative

            if number > (2 ** 31 - 1) // 10 or (number == (2 ** 31 - 1) // 10 and value > 7): return 2 ** 31 - 1
            if number < - ((2 ** 31) // 10) or (number == - ((2 ** 31) // 10) and value < -8): return -2 ** 31

            number = number * 10 + value

        return number

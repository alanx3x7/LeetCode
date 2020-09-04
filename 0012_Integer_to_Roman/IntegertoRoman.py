class Solution:

    def intToRoman(self, num: int) -> str:

        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        huns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        mils = ["", "M", "MM", "MMM"]

        place = 0
        numeral = ""
        while num > 0:

            last = num % 10
            num = num // 10

            if place == 0: numeral = ones[last] + numeral
            if place == 1: numeral = tens[last] + numeral
            if place == 2: numeral = huns[last] + numeral
            if place == 3: numeral = mils[last] + numeral

            place += 1

        return numeral

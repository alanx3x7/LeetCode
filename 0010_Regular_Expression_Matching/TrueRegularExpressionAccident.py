# Accidentally implemented the real regular expression

class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        if s == p or p == "*":
            return True

        while not p == "":
            literal = p[0]

            if literal == ".":
                return self.isMatch(s[1:], p[1:])

            elif 96 < ord(literal) < 123:
                if s == "" or s[0] != literal:
                    return False
                p = p[1:]
                s = s[1:]

            elif literal == "*":
                for i in range(len(s)):
                    if p[1:] == "":
                        return True
                    if self.isMatch(s[i:], p[1:]):
                        return True
                return False


            else:
                return False

        return s == ""
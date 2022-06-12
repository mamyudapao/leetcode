class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        i , digit = 0, 0
        for c in abbr:
            if c.isdigit():
                if digit == 0 and c == '0':
                    return False
                digit = digit * 10 + int(c)
            else:
                if digit:
                    i += digit
                    digit = 0
                if i >= len(word) or word[i] != c:
                    return False
                i += 1
        if digit:
            i += digit

        return i == len(word)
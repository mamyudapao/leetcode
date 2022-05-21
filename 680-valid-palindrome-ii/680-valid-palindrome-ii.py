class Solution:
  def validPalindrome(self, s):
    def check_palindrome(s, pointer1, pointer2):
      while pointer1 < pointer2:
        if s[pointer1] == s[pointer2]:
          pointer1 += 1
          pointer2 -= 1
        else:
          return False
      return True
    pointer1 = 0
    pointer2 = len(s) -1
    while pointer1 < pointer2:
      if s[pointer1] != s[pointer2]:
        return check_palindrome(s, pointer1 + 1, pointer2) or check_palindrome(s, pointer1, pointer2 - 1)
      pointer1 += 1
      pointer2 -= 1
    return True
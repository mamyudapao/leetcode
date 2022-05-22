class Solution:
  def validPalindrome(self, s):
    def isPalindrome(s, left, right):
      while left < right:
        if s[left] != s[right]:
          return False
        left += 1
        right -= 1
      return True
    left = 0
    right = len(s) - 1
    while left < right:
      # だめだった場合の処理
      if s[left] != s[right]:
        return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)
      left += 1
      right -= 1
    return True
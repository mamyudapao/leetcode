class Solution:
  def reverseString(self, s):
    def helper(s, left, right):
      if left < right:
        s[left], s[right] = s[right], s[left]
        helper(s, left + 1, right - 1)
    
    helper(s, 0, len(s)-1)
    return s
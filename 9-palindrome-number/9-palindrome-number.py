class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is a negative number it is not a palindrome
        # If x % 10 = 0, in order for it to be a palindrome the first digit should
        if x < 0 or (x > 0 and x % 10 == 0):
          return False
        
        reversedNum = 0
        while x > reversedNum:
          reversedNum = reversedNum * 10 + x % 10
          x = x // 10
          
        if x == reversedNum or x == reversedNum//10:
          return True
        else:
          return False
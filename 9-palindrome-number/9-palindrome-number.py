class Solution:
    def isPalindrome(self, x: int) -> bool:
      if x < 0 or (x > 0 and x % 10 == 0):
        return False
      check_num = 0
      
      while x > check_num:
        check_num = check_num * 10 + x % 10
        x = x //10
      return x == check_num or x == check_num // 10
from collections import deque
class Solution:
  def isPalindrome(self, x: int) -> bool:
    stack = []
    for i in str(x):
        stack.append(i)
    result = ""
    for i in range(len(stack)):
        result = result + stack.pop()
    if result == str(x):
        return True
    return False

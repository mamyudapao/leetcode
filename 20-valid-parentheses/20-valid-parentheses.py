hashMap = {
  ')': '(',
  '}': '{',
  ']': '['
}

class Solution:
  def isValid(self, s: str) -> int:
    stack = []
    for i in range(len(s)):
      if s[i] in ['[', '(', '{']:
        stack.append(s[i])
      else:
        if len(stack) == 0 or  hashMap[s[i]] !=stack.pop():
          return False
    if len(stack) == 0:
      return True
    return False
class Solution:
  def isValid(self, s: str) -> bool:
    hashMap = {')': '(', '}':'{', ']': '[' }
    stack = []
    for i in range(len(s)):
      if s[i] in ['[', '{', '(']:
        stack.append(s[i])
      else:
        if len(stack) == 0: return False
        if hashMap[s[i]] != stack.pop():
            return False
    if len(stack) == 0:
        return True
    return False
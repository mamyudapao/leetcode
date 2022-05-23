hashMap = {
  ')': '(',
  '}': '{',
  ']': '[',
}

class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    for i in range(len(s)):
      if s[i] in ['[', '{', '(']:
        stack.append(s[i])
      elif not stack or stack.pop() != hashMap[s[i]]:
        return False
    if len(stack) == 0:
      return True
    return False
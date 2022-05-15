class Solution:
  def isValid(self, s: str) -> bool:
    mpp = {')': '(', '}': '{', ']': '['}
    stk = []
    for e in s:
      if e in mpp:
        if stk and stk[-1] == mpp[e]:
          stk.pop()
        else:
          return False
      else:
        stk.append(e)
    if(len(stk) > 0):
      return False
    return True
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = str(x)
        stack = []
        for i in range(len(x)):
          stack.insert(0, x[i])
        if x == "".join(stack): return True
        return False
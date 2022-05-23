
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
      index = 0
      sum = 0 
      while index < len(s):
        if index+1 <len(s) and values[s[index]] < values[s[index + 1]]:
          sum += values[s[index+1]] - values[s[index]]
          index += 2
        else:
          sum += values[s[index]]
          index += 1
      return sum
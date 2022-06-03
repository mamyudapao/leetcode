class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
      result = []
      for i in range(n):
        txt = ""
        if (i+1) % 3 == 0:
          txt += "Fizz"
        if (i+1) % 5 == 0:
          txt += "Buzz"
        if txt == "":
          result.append(str(i+1))
        else:
          result.append(txt)
      return result
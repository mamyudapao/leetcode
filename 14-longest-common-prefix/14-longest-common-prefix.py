class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      if len(strs) == 1:
        return strs[0]
      result = ""
      target = strs[0]
      for i in range(len(target)):
        for str in strs:
          if  i == len(str) or str[i] != target[i] :
            return result
        result += target[i]
      return result
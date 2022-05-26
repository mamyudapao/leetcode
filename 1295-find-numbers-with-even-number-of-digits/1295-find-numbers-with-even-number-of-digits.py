class Solution:
    def findNumbers(self,nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
          value = nums[i]
          number = 0
          while value > 0:
            value //= 10
            number +=1
          if number%2 == 0:
            counter += 1
        return counter
class Solution:
    def findNumbers(self,nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            number = nums[i]
            counter = 0
            while number > 0:
                number //= 10
                counter += 1
            if counter % 2 == 0:
                cnt +=1
        return cnt
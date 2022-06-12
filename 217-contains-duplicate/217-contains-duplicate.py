class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_set = set()
        
        for i in range(len(nums)):
          if nums[i] in check_set:
            return True
          else:
            check_set.add(nums[i])
        return False
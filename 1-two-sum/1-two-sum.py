class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
          if target - nums[i] in hash_table:
            return [i, hash_table[target - nums[i]]]
          hash_table[nums[i]] = i
        return -1
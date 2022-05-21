class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    checked_map = {}
    for i in range(len(nums)):
      remain = target - nums[i]
      if remain in checked_map:
        return [i, checked_map[remain]]
      checked_map[nums[i]] = i
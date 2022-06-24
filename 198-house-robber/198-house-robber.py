class Solution:
  
  def __init__(self) -> None:
    self.memo = {}
    
  def rob(self, nums: List[int]) -> int:
    self.memo = {}
    return self.robFrom(0, nums)
  
  def robFrom(self, i, nums):
    
    # これ以上調べる家がない場合 
    if i >= len(nums):
      return 0
    
    if i in self.memo:
      return self.memo[i]
    
    ans = max(self.robFrom(i+1, nums), self.robFrom(i+2, nums) + nums[i])
    # Cache for future use.
    self.memo[i] = ans
    return ans
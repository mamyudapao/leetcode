class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            index = (left + right)//2
            if isBadVersion(index):
                right = index
            else:
                left = index + 1
            
        return left
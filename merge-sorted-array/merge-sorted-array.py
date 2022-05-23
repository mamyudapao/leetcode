class Solution:   
    def merge(self,nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new_size = m + n
        current_size = m
        pointer = 0
        for i in range(m, new_size):
            nums1[i] = nums2[pointer]
            pointer +=1
        nums1.sort()
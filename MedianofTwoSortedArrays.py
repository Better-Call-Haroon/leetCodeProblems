class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size=max(len(nums1),len(nums2))
        nums3=nums1+nums2            
        nums3.sort()
        if len(nums3)%2!=0:
            return nums3[len(nums3)//2]
        else:
            middle_index = len(nums3) // 2
            return (nums3[middle_index-1] + nums3[middle_index]) / 2.0

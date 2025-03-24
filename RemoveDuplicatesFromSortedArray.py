class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set1 = sorted(set(nums))
        nums[:len(set1)] = set1
        return len(set1)
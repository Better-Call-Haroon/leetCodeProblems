import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        set1=set(permutations(nums))
        return list(set1)
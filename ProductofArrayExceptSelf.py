
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        n = len(nums)

        if zero_count > 1:
            return [0] * n

        total_product = 1
        for i in nums:
            if i != 0:
                total_product *= i

        return [0 if zero_count == 1 and i != 0 else total_product // i if i != 0 else total_product for i in nums]


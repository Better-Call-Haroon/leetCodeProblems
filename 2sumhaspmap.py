class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in hashtable:
                return [i,hashtable[rem]]
            hashtable[nums[i]]=i
            








class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        total=int()
        anotherList=[]
        size=len(nums)
        hashMap={}
        i=0
        
        for i in range(size-1):
            total=nums[i]+nums[i+1]
            anotherList=nums[i]
            i=i-1
            hashMap[total]=anotherList
        total=target
        if target in hashMap:
            print(hashMap[target])
            


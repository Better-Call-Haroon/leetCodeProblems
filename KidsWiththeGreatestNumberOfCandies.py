class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candiesPluser=[]
        size=len(candies)

        maxcandies=max(candies)
        finalList=[]
        for i in range(0,size):
            candiesPluser.append(candies[i]+extraCandies)
        for i in range(0,size):
            if candiesPluser[i]>=maxcandies:
                finalList.append(True)
            else:
                finalList.append(False)
        return finalList
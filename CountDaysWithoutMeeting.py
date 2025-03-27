class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
      
        lastday=0
        reserve=0
        for i in meetings:
            if i[0] > lastday:
                reserve += i[0]-lastday-1
               
                lastday = i[1]
                
            else:
                lastday = max(lastday, i[1])
               
        if(lastday < days):
            reserve += days-lastday
        return reserve
        


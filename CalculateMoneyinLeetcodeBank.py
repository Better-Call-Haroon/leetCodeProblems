class Solution:
    def totalMoney(self, n: int) -> int:
        daycount = 0
        moneycount = 0
        moneylist = []
        for i in range(n):
            temp = moneycount + daycount+1
            moneylist.append(temp)
            daycount += 1

            if daycount == 7:
                daycount = 0
                moneycount += 1

        print(moneylist)
        return sum(moneylist)

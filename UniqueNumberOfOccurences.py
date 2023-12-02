class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashtable={}
        seen_values=set()
        for i in arr:
            if i not in hashtable:
                hashtable[i]=1
            else:
                hashtable[i]+=1

        for value in hashtable.values():
            if value in seen_values:
                return False
            seen_values.add(value)
    
        return True


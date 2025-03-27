class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable={}
        list_sorted=[]
    
        for i in strs:
            key="".join(sorted(i))
            if key  not in hashtable:
                hashtable[key]=[]
            hashtable[key].append(i)


        return list(hashtable.values())
                
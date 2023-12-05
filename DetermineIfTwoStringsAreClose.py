class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)!=set(word2):
            return False
        freq1=collections.Counter(word1)
        freq2 = collections.Counter(word2)        
        return sorted(freq1.values()) == sorted(freq2.values())

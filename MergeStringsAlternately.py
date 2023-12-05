class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list1 = list(word1)
        list2 = list(word2)
        size = 2 * max(len(list1), len(list2))
        list3 = [''] * size
        even = 0
        odd = 1

        for i in range(len(list1)):
            list3[even] = list1[i]
            even += 2

        for j in range(len(list2)):
            list3[odd] = list2[j]
            odd += 2

        return ''.join(list3)

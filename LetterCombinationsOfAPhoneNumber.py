class Solution:
    def letterCombinations(self, digits: str) -> list:
        phone_numbers = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                         "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []

        final_list=[phone_numbers[i] for i in digits if i in phone_numbers]

        result=[""]
        for chars in final_list:
            result=[prefix + char for prefix in result for char in chars]

        return result
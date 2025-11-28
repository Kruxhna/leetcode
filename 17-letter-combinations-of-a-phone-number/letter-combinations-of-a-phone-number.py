class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits :
            return []
        
        phone = {
            "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"
        }

        res = []

        def backtrack(idx,curr_str) :
            if len(curr_str) == len(digits) :
                res.append(curr_str)
                return

            curr_di = digits[idx]
            possible_l = phone[curr_di]

            for l in possible_l :
                backtrack(idx+1,curr_str+l)
            

        backtrack(0,"")
        return res
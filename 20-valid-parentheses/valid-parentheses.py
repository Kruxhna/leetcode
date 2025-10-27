class Solution(object):
    def isValid(self, s):
        stack = []

        close_to_open = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for char in s :
            if char in close_to_open :
                if not stack :
                    return False
                top_ele = stack.pop()

                if top_ele != close_to_open[char] :
                    return False
            else :
                stack.append(char)
        return not stack
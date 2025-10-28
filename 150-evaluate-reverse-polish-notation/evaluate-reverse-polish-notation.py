class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []

        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    result = int(a / b)

                stack.append(result)
    
            else:
                stack.append(int(token))

        return stack[0]
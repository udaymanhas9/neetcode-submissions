class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["-","+","*","/"]
        for t in tokens:
            if t in operators:
                num1, num2 = stack.pop(), stack.pop()
                
                if t == "+":
                    res = num1+num2
                elif t == "-":
                    res = num2-num1
                elif t == "*":
                    res = num1*num2
                else:
                    res = int(num2/num1)
                stack.append(res)
            else:
                stack.append(int(t))

        return stack[-1]
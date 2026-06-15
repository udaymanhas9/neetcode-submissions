class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']':'[', '}':'{'}
        stack = deque()
        if len(s) % 2 != 0:
            return False
        for bracket in s:
            if bracket in ('(','[','{'):
                stack.append(bracket)
            else:
                if stack:
                    left = stack.pop()
                else:
                    return False
        
                if  left != dic[bracket]:
                    print(left)
                    print(bracket)
                    print(stack)
                    return False
        return True if not stack else False
                

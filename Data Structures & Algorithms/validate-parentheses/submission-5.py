class Solution:
    def isValid(self, s: str) -> bool:
        q = deque([])
        mapping = {'(':')', '[':']', '{':'}'} 
        
        for bracket in s:
            if bracket in mapping:
                q.appendleft(mapping[bracket])
            else:
                if q :
                    if bracket != q.popleft():
                        return False
                else:
                    return False

        return len(q) == 0
        
                    
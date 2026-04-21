class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True) # Sorting by position
        stack = []
        
        for p,s in pair: # Reverse Sorted Order
            stack.append((target-p)/s) # This is the time taken to reach target
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
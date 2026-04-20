class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n        
        zero_seen = (False,0)
        prod = 1
        for i, num in enumerate(nums):
            if num == 0:
                print("hey")
                
                if zero_seen[0]:
                    print("Returning at 1")
                    return ans
                zero_seen = (True, i)
                continue
            prod *= num
        
        if zero_seen[0]:
            ans[zero_seen[1]] = prod
            print("Returning at 2")
            return ans
        
        for i, num in enumerate(nums):
            
            ans[i] = int(prod/num)
        print("Returning at 3")
        return ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n        
        zero_seen = None
        prod = 1
        for i, num in enumerate(nums):
            if num == 0:
                
                if zero_seen is not None:
                    return ans
                zero_seen = i
                continue
            prod *= num
        
        if zero_seen:
            ans[zero_seen] = prod
            return ans
        
        for i, num in enumerate(nums):
            ans[i] = int(prod/num)
        return ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0]* len(nums)
        prod = 1
        
        zeros = []

        for i, num in enumerate(nums):
            if num != 0:
                prod *= num
            else:
                zeros.append(i)
        if len(zeros) >= 2:
            pass
        elif len(zeros) == 1:
            res[zeros[0]] = prod
        else:
            for i, num in enumerate(nums):
                res[i] = int(prod / num)
        
        return res
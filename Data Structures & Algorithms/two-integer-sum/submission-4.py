class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dic = {}
        
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in _dic:
                return [_dic[remainder], i]
            _dic[num] = i
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        _dic = defaultdict(int)
        for i, num in enumerate(numbers):
            remainder = target - num
            
            if remainder in _dic:
                return [_dic[remainder], i+1]
            _dic[num] = i +1
        
                
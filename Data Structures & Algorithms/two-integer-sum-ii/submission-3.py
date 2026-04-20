class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        _dic = defaultdict(int)
        for i, num in enumerate(numbers):
            
            if target - num in _dic:
                return [_dic[target - num], i+1]
            _dic[num] = i +1
        
                
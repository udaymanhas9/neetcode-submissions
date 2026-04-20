class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        _dic = defaultdict(int)
        for num in nums:
            _dic[num] += 1
        
        # for key in _dic:
            # ans.append([ _dic[key], key])
        
        _dic_1 = sorted(_dic.items(), key = lambda item:item[1], reverse = True)[:k]
        
        return [item[0] for item in _dic_1] 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)

        res = sorted(dic, key=dic.get, reverse = True)[:k]
        
        return res

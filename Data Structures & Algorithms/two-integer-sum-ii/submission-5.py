class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(numbers):
            remainder = target - num
            if remainder in dic:
                return [dic[remainder], i+1]
            dic[num] = i+1
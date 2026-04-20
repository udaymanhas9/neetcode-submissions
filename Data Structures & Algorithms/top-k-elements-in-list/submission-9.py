class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        l = []

        for i,j in a.items():
            heapq.heappush(l,(-j,i))
        print(l)
        final = []
        for i in range(k):
            see= heapq.heappop(l)
            final.append(see[1])
        return final
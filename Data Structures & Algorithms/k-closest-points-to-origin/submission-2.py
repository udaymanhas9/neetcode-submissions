class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        _dic = defaultdict(list)
        heap = []
        ans = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)**(0.5)
            _dic[-dist].append(point)
            heapq.heappush(heap, -dist)
        while len(heap) > k:
            heapq.heappop(heap)
        for dist in set(heap):
            ans.extend(_dic[dist]) 
        return ans

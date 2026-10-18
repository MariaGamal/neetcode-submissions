import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build max heap and popk times
        d = defaultdict(int)
        for num in nums:
            d[num] = d.get(num, 0) - 1
        maxHeap = [(value, key) for key, value in d.items()]
        heapq.heapify(maxHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res

        
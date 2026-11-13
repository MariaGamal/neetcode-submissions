import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.minHeap = []
        self.k = k
        for i in range(min(k, len(nums))):
            heapq.heappush(self.minHeap, nums[i])
            self.k -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #k or k ++
        if self.k > 0:
            self.k -=1
        else:
            heapq.heappop(self.minHeap) 
        return self.minHeap[0]
        

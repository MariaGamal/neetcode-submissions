class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            mid = l + ((r-l) // 2)
            curH = 0
            for num in piles:
                curH += math.ceil(num/mid)
            if curH <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

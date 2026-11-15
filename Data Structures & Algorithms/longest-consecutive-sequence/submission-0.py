class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in s:
                cur = 1
                while num + 1 in s:
                    cur +=1
                    num +=1
                res = max(res, cur)
        return res
        
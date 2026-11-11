class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            new  = []
            for cur in ans:
                new.append(cur + [num])
            ans.extend(new)
        return ans
        
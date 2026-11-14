class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, index, total):
            if index >= len(nums): return 
            if total > target: return
            if total == target:
                res.append(cur.copy())
                return
            cur.append(nums[index])
            dfs(cur, index, total + nums[index])
            cur.pop()
            dfs(cur, index + 1, total)

        dfs([], 0, 0)
        return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(cur, index):
            if index >= len(nums): return 
            if sum(cur) + nums[index] > target: return
            if sum(cur) + nums[index] == target:
                cur.append(nums[index])
                res.append(cur.copy())
                cur.pop()
                return
            cur.append(nums[index])
            dfs(cur, index)
            cur.pop()
            dfs(cur, index + 1)

        dfs([], 0)
        return res
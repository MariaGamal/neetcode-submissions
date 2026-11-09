# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        curMax = root.val

        def dfs(root):
            nonlocal ans, curMax
            if not root: return
            if root.val >= curMax:
                ans +=1
                curMax = root.val
            prev = curMax
            dfs(root.left)
            curMax = prev
            dfs(root.right)
            return ans

        dfs(root)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        depth = 0
        q = deque([[root]])
        while q[0]:
            depth +=1
            level = q.popleft()
            cur = []
            for node in level:
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            q.append(cur)
        return depth
        
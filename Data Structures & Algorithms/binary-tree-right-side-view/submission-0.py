# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = [root.val]
        q = deque([(deque([root]), 1)])
        while q:
            (nodes, count) = q.popleft()
            newcount = 0
            newnodes = deque()
            while count:
                node = nodes.popleft()
                if node.left:
                    newnodes.append(node.left)
                    newcount +=1
                if node.right:
                    newnodes.append(node.right)
                    newcount +=1
                count -=1
            if newcount:
                q.append((newnodes, newcount))
                res.append(newnodes[-1].val)
        return res
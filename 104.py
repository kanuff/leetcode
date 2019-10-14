class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        depths = [0]
        depths.append(self.maxDepth(root.left))
        depths.append(self.maxDepth(root.right))
        return max(depths) + 1
        
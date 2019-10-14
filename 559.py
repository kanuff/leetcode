class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None: return 0
        
        children = root.children
        depths = [0]
        for child in children:
            depths.append(self.maxDepth(child))
        return max(depths) + 1
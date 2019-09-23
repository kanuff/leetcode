class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortHeights = sorted(heights)
        return sum(1 for x,y in zip(sortHeights, heights) if x != y)
        
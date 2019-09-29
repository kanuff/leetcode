class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {b:i for i,b in enumerate(arr2)}
        return sorted(arr1, key = lambda x: order.get(x, x+1000))
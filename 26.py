class Solution:
    # doesn't work
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        e = 1
        n = 0
        l = len(nums) - 1
        while n != l:
            if nums[n] in nums[:e]:
                if nums[l] not in nums[:e]:
                    nums[n], nums[l] = nums[l], nums[n]
                    l-=1
                    e+=1
                    n+=1
                else: 
                    l-=1
            else:
                e+=1
                n+=1
        return len(nums[:e])

        
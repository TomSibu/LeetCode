class Solution:
    def check(self, nums: List[int]) -> bool:
        drop = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drop += 1
                if drop > 1:
                    return False
        return True

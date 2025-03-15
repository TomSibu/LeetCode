class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left=1
        right=10**9
        while left<right:
            mid, t, i = (left+right)//2, 0, 0
            while i< len(nums) and t<k:
                if nums[i]<=mid:
                    t+=1
                    i+=2
                else:
                    i+=1
            left, right = (mid+1, right) if t<k else (left,mid)
        return left
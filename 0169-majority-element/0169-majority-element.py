class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)/2
        for i in set(nums):
            if nums.count(i)>=n:
                return i
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        mod = nums[0] % x

        if any(num % x != mod for num in nums):
            return -1

        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(num - median) // x for num in nums)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0

        while nums[0] < k: 
            if len(nums) < 2:
                return -1  

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            newValue = x * 2 + y
            heapq.heappush(nums, newValue)

            operations += 1

        return operations
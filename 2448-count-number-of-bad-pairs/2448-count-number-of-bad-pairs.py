from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2 
        good_pairs = 0
        diff_count = {} 

        for i in range(n):
            diff = i - nums[i]  
            
            if diff in diff_count:
                good_pairs += diff_count[diff] 
            
            diff_count[diff] = diff_count.get(diff, 0) + 1

        return total_pairs - good_pairs 
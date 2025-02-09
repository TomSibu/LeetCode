class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        count = 0 
        length = len(nums)
        nums_new = [ num - index for index, num in enumerate(nums)]

        count = Counter(nums_new)
      
        total_pairs = length*(length-1)/2 

        for key, val in count.items(): 

            if val!=1: 
                #print ('val', val)
                total_pairs -= val*(val-1)/2

        return int(total_pairs)

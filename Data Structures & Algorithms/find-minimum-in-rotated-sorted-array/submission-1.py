class Solution:
    def findMin(self, nums: List[int]) -> int:
                
        L = 0
        R = len(nums) - 1 
        
        while L < R:
            ptr = (L + R) // 2

            if nums[ptr] > nums[R]:
                L = ptr + 1
            else:
                R = ptr
            
        return nums[L]
            
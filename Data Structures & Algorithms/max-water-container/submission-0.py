class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxVolume = 0

        pointer1 = 0
        pointer2 = len(heights) - 1



        # 1 , 7 , 2 , 5 , 4 , 7 , 3 , 6

        # 1 , 1 (6) * 8

        # 6 (7) , 6 * 7

        while pointer1 != pointer2:

            maxVolume = max(maxVolume, min(heights[pointer1], heights[pointer2]) * (pointer2 - pointer1 ))

            if heights[pointer1] <= heights[pointer2]:
                pointer1 += 1
            else: 
                pointer2 -= 1
        
        return maxVolume
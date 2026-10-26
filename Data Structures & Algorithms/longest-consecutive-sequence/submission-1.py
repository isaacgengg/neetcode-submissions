class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seenNums = set(nums)
        
        res = 0

        for key in seenNums:
            if key - 1 in seenNums:
                continue
            
            currentKey = key
            currSeq = 1
            while currentKey + 1 in seenNums:
                currentKey += 1
                currSeq += 1

            res = max(res, currSeq)

        return res

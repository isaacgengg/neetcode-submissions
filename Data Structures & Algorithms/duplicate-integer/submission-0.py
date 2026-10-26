class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()

        for i in range(math.ceil(len(nums) // 2)): 
            if nums[i] == nums[-1 - i]:
                return True
            elif nums[i] in seenNums or nums[-1 - i] in seenNums :
                return True
            else:
                seenNums.add(nums[i])
                seenNums.add(nums[-1 - i])

        return False
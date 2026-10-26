class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        result = [0] * 2
        r = len(numbers) - 1
        l = 0

        while l < r:
            if numbers[l] > target - numbers[r]:
                r -= 1
                continue
            elif numbers[l] + numbers[r] == target:
                result[0] = l + 1
                result[1] = r + 1
                return result

            l += 1
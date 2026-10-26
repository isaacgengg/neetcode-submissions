class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1

        1 * 4 + 3

        while l <= r:
            middle = (l + r) // 2
            middleVal = matrix[middle // cols][middle % cols]

            if middleVal == target:
                return True
            elif middleVal < target:
                l = middle + 1
            else:
                r = middle - 1
        
        return False
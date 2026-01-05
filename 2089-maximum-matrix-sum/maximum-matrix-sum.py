class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        neg_count = 0
        min_abs = float('inf')
        
        for row in matrix:
            for val in row:
                abs_val = abs(val)
                total_sum += abs_val
                if abs_val < min_abs:
                    min_abs = abs_val
                if val < 0:
                    neg_count += 1
                    
        if neg_count % 2 == 0:
            return total_sum
        return total_sum - 2 * min_abs
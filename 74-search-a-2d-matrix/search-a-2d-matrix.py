class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0] :
            return False

        n = len(matrix)
        m = len(matrix[0])

        l,h = 0,n*m-1

        while l <= h :
            mid = l + (h-l)//2
            row = mid//m
            col = mid%m

            mid_val = matrix[row][col]

            if mid_val == target :
                return True 
            elif mid_val > target :
                h = mid-1
            else :
                l = mid+1
        return False 
        
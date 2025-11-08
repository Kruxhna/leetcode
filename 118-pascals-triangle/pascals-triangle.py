class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        if numRows == 1 :
            return triangle

        for i in range(1,numRows) :
            prev_r = triangle[-1]
            new_r = [1]

            for j in range(len(prev_r)-1) :
                new_num = prev_r[j]+prev_r[j+1]
                new_r.append(new_num)

            new_r.append(1)

            triangle.append(new_r)

        return triangle
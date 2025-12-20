class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0,0]

        for student in students :
            count[student] += 1
        for i, sandwich in enumerate(sandwiches) :
            if count[sandwich] > 0 :
                count[sandwich] -= 1
            else :
                return len(sandwiches)-i
        return 0
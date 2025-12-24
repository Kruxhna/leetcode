class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_cap = sum(apple)
        capacity.sort(reverse= True)

        box = 0 
        for cap in capacity :
            total_cap -= cap
            box += 1
            if total_cap <= 0 :
                break
        return box
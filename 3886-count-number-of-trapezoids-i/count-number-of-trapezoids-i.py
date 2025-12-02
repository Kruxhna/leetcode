from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
       
        y_counts = defaultdict(int)
        for x, y in points:
            y_counts[y] += 1
        
        level_segments = []
        for count in y_counts.values():
            if count >= 2:
                ways = count * (count - 1) // 2
                level_segments.append(ways)
        
        total_trapezoids = 0
        current_sum = 0
        
        for segments in level_segments:
            total_trapezoids = (total_trapezoids + segments * current_sum) % MOD
            current_sum = (current_sum + segments) % MOD
            
        return total_trapezoids
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        event = []
        
        for _ , y , l in squares :
            total_area += l*l
            event.append((y,l))
            event.append((y+l,-l))

        if total_area == 0 :
            return 0.0
        event.sort()

        target_area = total_area/2.0
        curr_a = 0.0
        curr_w = 0

        for i in range(len(event)-1) :
            y,change_w = event[i]
            curr_w += change_w

            next_y = event[i+1][0]
            h_diff = next_y -y

            if h_diff == 0 :
                continue

            area_in_strip = curr_w*h_diff

            if area_in_strip + curr_a >= target_area :
                return y+(target_area-curr_a) / curr_w
            curr_a += area_in_strip

        return float(event[-1][0])

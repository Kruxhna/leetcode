class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        x_coords = set()
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
        
        sorted_x = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        num_x = len(sorted_x)
        
        tree_cnt = [0] * (4 * num_x)
        tree_len = [0.0] * (4 * num_x)

        def update(v, tl, tr, l, r, add):
            if l >= r:
                return
            if l == tl and r == tr:
                tree_cnt[v] += add
            else:
                tm = (tl + tr) // 2
                update(2 * v, tl, tm, l, min(r, tm), add)
                update(2 * v + 1, tm, tr, max(l, tm), r, add)
            
            if tree_cnt[v] > 0:
                tree_len[v] = float(sorted_x[tr] - sorted_x[tl])
            elif tr - tl > 1:
                tree_len[v] = tree_len[2 * v] + tree_len[2 * v + 1]
            else:
                tree_len[v] = 0.0

        y_events = []
        for x, y, l in squares:
            y_events.append((y, x, x + l, 1))
            y_events.append((y + l, x, x + l, -1))
        
        y_events.sort()

        total_area = 0.0
        for i in range(len(y_events) - 1):
            y, x1, x2, delta = y_events[i]
            update(1, 0, num_x - 1, x_map[x1], x_map[x2], delta)
            slab_h = y_events[i+1][0] - y
            total_area += tree_len[1] * slab_h
        
        for v in range(len(tree_cnt)):
            tree_cnt[v] = 0
            tree_len[v] = 0.0
            
        target_area = total_area / 2.0
        curr_area = 0.0
        
        for i in range(len(y_events) - 1):
            y, x1, x2, delta = y_events[i]
            update(1, 0, num_x - 1, x_map[x1], x_map[x2], delta)
            
            slab_h = y_events[i+1][0] - y
            slab_area = tree_len[1] * slab_h
            
            if curr_area + slab_area >= target_area - 1e-11:
                if tree_len[1] > 0:
                    res = y + (target_area - curr_area) / tree_len[1]
                    return max(float(y), res)
                return float(y)
                
            curr_area += slab_area
            
        return float(y_events[-1][0])
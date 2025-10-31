class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for p,s in zip(position,speed) :
            time_of_arrival = (target-p)/ s
            cars.append((p,time_of_arrival))

        cars.sort(key= lambda x : x[0],reverse= True)
        stack = []

        for p,time in cars :
            if not stack :
                stack.append(time)
                continue

            if time > stack[-1] :
                stack.append(time)

        return len(stack)    
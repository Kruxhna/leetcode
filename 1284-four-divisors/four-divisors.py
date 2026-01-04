import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0 

        for num in nums :
            divisor = set()

            for i in range(1,int(math.sqrt(num))+1) :
                if num%i == 0 :
                    divisor.add(i)
                    divisor.add(num//i)

                if len(divisor) > 4 :
                    break
            
            if len(divisor) == 4 :
                total_sum += sum(divisor)

        return total_sum
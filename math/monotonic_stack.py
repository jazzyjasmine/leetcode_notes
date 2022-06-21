from typing import List


class Solution739:
    def dailyTemperatures_normal_sol(self, temperatures: List[int]) -> List[int]:
        # Time O(n), Space O(n)
        stack = []
        ans = [0] * len(temperatures)
        
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev_index = stack.pop()
                ans[prev_index] = index - prev_index
            stack.append(index)
        
        return ans
    
    def dailyTemperatures_optimized_sol(self, temperatures: List[int]) -> List[int]:
        # Time O(n), Space O(1)
        # reference: https://leetcode.com/problems/daily-temperatures/solution/
        ans = [0] * len(temperatures)
        hottest_temp = -1
        
        for day_index in range(len(temperatures) - 1, -1, -1):
            if temperatures[day_index] >= hottest_temp:
                ans[day_index] = 0
                hottest_temp = temperatures[day_index]
                continue
                
            days = 1
            while temperatures[day_index + days] <= temperatures[day_index]:
                days += ans[day_index + days]
            ans[day_index] = days
        
        return ans
        
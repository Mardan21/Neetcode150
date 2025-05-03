class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_idx, stack_temp = stack.pop()
                res[stack_idx] = idx - stack_idx
            stack.append([idx, temp])
        return res

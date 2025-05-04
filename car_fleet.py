class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_pairs = [[pos, speed] for pos, speed in zip(position, speed)]

        stack = []
        for pos, speed in sorted(car_pairs)[::-1]: 
            time_to_target = (target - pos) / speed
            stack.append(time_to_target) 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


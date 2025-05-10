class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Pair up each car's position and speed
        pair = [[p, s] for p, s in zip(position, speed)]


        # 2. Sort cars from closest to target (highest position) to farthest (lowest position)
        pair.sort(reverse=True)

        # 3. Stack to track fleets
        stack = []

        # 4. Go through each car
        for p, s in pair: 
            # Time = Distance / Speed
            time = (target - p) / s
            stack.append(time)

            # If this car catches up to the fleet in front, merge them
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Remove the merged car's time

        # 5. Remaining items in stack = number of fleets
        return len(stack)

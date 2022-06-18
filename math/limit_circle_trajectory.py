class Solution1041:
    # 1041. Robot Bounded In Circle
    # https://leetcode.com/problems/robot-bounded-in-circle/solution/
    # Time O(n), Space O(1)
    # Properties of limit circle trajectory:
    # 1. If the robot returns to the initial point after one cycle, then limit cycle trajectory.
    # 2. If the robot doesn't face north at the end of the first cycle, then limit cycle trajectory.
    # 3. After at most 4 cycles, the limit cycle trajectory returns to the initial point.
    # Proof: https://leetcode.com/problems/robot-bounded-in-circle/solution/#appendix-mathematical-proof
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        
        for instruction in instructions:
            if instruction == 'L':
                direction = (direction - 1) % 4
            elif instruction == 'R':
                direction = (direction + 1) % 4
            else:
                move = moves[direction]
                x += move[0]
                y += move[1]
        
        return direction != 0 or (x == 0 and y == 0)
        
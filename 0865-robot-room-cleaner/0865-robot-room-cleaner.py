# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """


        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        
        def backtrack(r,c,d):
            robot.clean()
            visited.add((r,c))


            for i in range(4):
                new_d = (d + i) % 4

                new_r, new_c = r + directions[new_d][0], c + directions[new_d][1]

                if (new_r, new_c) not in visited and robot.move():
                    backtrack(new_r, new_c, new_d)
                    go_back()
                
                robot.turnRight()
        
        backtrack(0,0, 0)


        
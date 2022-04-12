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
        self.grid = {}
        self.compass = {
          0: [-1, 0], # NORTH
          1: [1, 0],  # SOUTH
          2: [0, -1], # WEST
          3: [0, 1]   # EAST
          }

        self.backtrack(robot, 0, 0, 0)
        print("I finished cleaning.")
    compass = {}
 
    def backtrack(self, robot, row, col, direction):
      self.grid[(row,col)] = True
      print("I am at", row, col)
      robot.clean()
      print("I am cleaning")
      # direction = (1,2,3,4,5,6,7,8,9,10)

      for option in ['straight', 'left', 'right', 'back']:
       print("Considering going", option)
       if option == 'straight':
          print("I am going straight.")
       elif option == 'left':
          print("I am turning left.")
          robot.turnLeft()
          if direction == 0:
            print("I am now facing west")
            direction = 2
          elif direction == 1:
            print("I am now facing east")
            direction = 3
          elif direction == 2:
            print("I am now facing south")
            direction = 1
          else:
            print("I am now facing north")
            direction = 0
       elif option == 'right':
          robot.turnRight()
          robot.turnRight() # I think I do it twice bc of turnLeft
          print("I turned right whatever that means.")
          print("I am really doing a 180")
          if direction == 0:
            print("I am now facing south")
            direction = 1
          elif direction == 1:
            print("I am now facing north")
            direction = 0
          elif direction == 2:
            print("I am now facing east")
            direction = 3
          else:
            print("I am now facing west")
            direction = 2
       elif option == 'back':
          print("I am turning backwards.")
          robot.turnRight()
          if direction == 0:
            print("I am now facing east")
            direction = 3
          elif direction == 1:
            print("I am now facing west")
            direction = 2
          elif direction == 2:
            print("I am now facing north")
            direction = 0
          else:
            print("I am now facing south")
            direction = 1
           
    
       next_row = row + self.compass[direction][0]
       next_col = col + self.compass[direction][1]

       if (next_row, next_col) in self.grid:
          print("I already cleaned the tile I am about to go onto.")
          continue

       if robot.move():
          # do something
          print("I moved")
          self.backtrack(robot, next_row, next_col, direction)
       else:
          print("I bumped into a wall. There's a wall at", next_row, next_col)
          self.grid[(next_row, next_col)] = False

      print("I exhausted straight, left, and right.")
      print("I am facing right of where I started.")
      print("I reached the end of the backtrack function.")
      print("... So I am backing up and then turning 180.")
      # end of all 4 boxes
      #robot.turnRight()
      robot.move()
      robot.turnLeft()
      robot.turnLeft()
      print("Now I am facing where I was before started this backtrack.")
      print("I think the grid looks like:")
      #print(self.grid)
      return

 

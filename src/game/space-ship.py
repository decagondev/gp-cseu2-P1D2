# add playing functionality
import sys
import random

# implement class to deal with the map
class Space:
# space class with rows and cols
    # constructor
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Allocate list to hold space
        self.space = [] # rows of space

        # iterate over the rows and add cols
        for _ in range(rows):
            newRow = ["."] * cols # array of 'cols' '.'s
            # append the row to space
            self.space.append(newRow)
        
        # throw some stars in about 7% of space
        starCount = int(rows * cols * 0.07)
        # work out 7% of map

        # iterate over stars
        for _ in range(starCount):
            # random row star
            rowNum = random.randint(0, len(self.space) - 1)
            # random col star
            colNum = random.randint(0, len(self.space) - 1)
            # add the '*' to space at row and col
            self.space[rowNum][colNum] = "*"
        
        # Add the ship
        self.shipRow = rows // 2
        self.shipCol = cols // 2

        # Kill any star at the ships location
        self.space[self.shipRow][self.shipCol] = "."


    # print map function
    def printMap(self):
        # iterate over space rows
        for r in range(self.rows):
            # iterate over space cols
            for c in range(self.cols):
                # check if the ship is in the grid space
                if r == self.shipRow and c == self.shipCol:
                    # draw the ship here
                    sys.stdout.write("Y ")
                # otherwise
                else:
                    # create a symbol from data in space list
                    symbol = self.space[r][c]
                    # write the col
                    sys.stdout.write(f"{symbol} ")
            
            print()


    # move ship function
    def moveShip(self, dir):
        # hold delta X and delta Y

        # convert direction to delta x and delta y
        
        # if direction is "N"
            # set delta Y to -1
        # else if direction is "S"
            # set delta Y to 1
        # else if direction is "W":
            # set delta X to -1
        # else if direction is "E":
            # set delta X to 1

        # increment ship col by delta x
        # increment ship row by delta y

        # bounds checking

        # if the ship to far col- set to zero
        # otherwise if ship too far col+ set to bounds - 1

         # if the ship to far row- set to zero
        # otherwise if ship too far row+ set to bounds - 1





        pass
# instantiate a space object
s = Space(10, 10)
# print the map
s.printMap()
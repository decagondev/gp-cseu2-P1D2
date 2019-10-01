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
            newRow = ['.'] * cols # array of 'cols' '.'s
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
            self.space[rowNum][colNum] = '*'
        
        # Add the ship

        # Kill any star at the ships location


    # print map function
    def printMap(self):
        # iterate over space rows
        for r in self.space:
            # iterate over space cols
            for c in r:
                # check if the ship is in the grid space
                    # draw the ship here
                # otherwise
                    # create a symbol from data in space list
                    # write the col

            # print empty line
            print()

# instantiate a space object
s = Space(10, 10)
# print the map
s.printMap()
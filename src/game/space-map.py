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
        for i in range(rows):
            newRow = ['.'] * cols # array of 'cols' '.'s
            # append the row to space
            self.space.append(newRow)
        
        # throw some stars in about 7% of space
        starCount = int(rows * cols * 0.07)
        # work out 7% of map

        # iterate over stars
        for i in range(starCount):
            # random row star
            rowNum = random.randint(0, len(self.space) - 1)
            # random col star
            colNum = random.randint(0, len(self.space) - 1)
            # add the '*' to space at row and col
            self.space[rowNum][colNum] = '*'

    # print map function
        # iterate over space rows
            # iterate over space cols
                # write the col
            # print empty line

# instantiate a space object

# print the map
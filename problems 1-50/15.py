'''
Starting in the top left corner of a 2x2 grid , and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

# Manhattan distance is going to be 20 + 20 = 40
# Always takes 20 down steps and 20 right steps to go from TL to BR

import math
# It's all the different ways you can choose 20 positions from 40
# Pick the 20 spots for R (or D), the rest must be the other direction
print(math.comb(40, 20))

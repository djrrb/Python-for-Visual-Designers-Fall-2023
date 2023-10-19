# draw a row of circles

# define our x count (and y count, for later use)
myXCount, myYCount = 10, 10
# define our shape dimensions
myShapeWidth, myShapeHeight = 100, 100

# visualize the range we are looping through
print(list(range(myXCount)))

# loop through our range of numbers
for myXNumber in range(myXCount):
    # get the x value by multiplying the column number (0–9)
    # by the shapeWidth
    myX = myXNumber * myShapeWidth
    # print our results
    print('col', myXNumber, myX)
    # draw the oval, oval(x, y, width, height)
    oval(myX, 0, myShapeWidth, myShapeHeight)
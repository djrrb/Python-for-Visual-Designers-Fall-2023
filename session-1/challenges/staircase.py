# make a staircase

# set some variables
# how many steps to draw?
myStepCount = 20
# the width of each step is equal to the full width divided by the step count
myWidth = width() / myStepCount
# each step with have a certain height, again equal to the full height divided by the step count
myStepHeight = height() / myStepCount

# we will create the staircase out of a series of rectangles that get increasingly tall
# so this variable will control the height of each rectangle, starting at the height of the first step
myHeight = myStepHeight

# the rectangles will move horizontally, so we have a variable for their x position
myX = 0

# make a new page
newPage()

# set the fill color to green
fill(0, 1, 0)

# make a background, which is a rectangle that starts at (0, 0) and covers the whole page
rect(0, 0, width(), height())

# set the color to magenta
fill(1, 0, 1)

# now let’s do a loop through the range of numbers between 0 and myStepCount, creating the myRect variable to represent the number we are on
for myRect in range(myStepCount):
    # draw a rectangle
    rect(myX, 0, myWidth, myHeight)
    # augment the X value so that the next rectangle is drawn to the right
    myX += myWidth
    # also augment myHeight value, so the next rectangle will be taller
    myHeight += myStepHeight
    
saveImage('staircase.png')
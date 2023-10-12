for myNumber in range(10): # loop through 10 numbers
    newPage(500, 1000) # make a new page
    fill(random(), random(), random()) # set a random color
    # draw a shape that’s half the width of the canvas
    myShapeWidth = width()/2
    # figure out the total horizontal margin left
    # by subtracting the shape width from the canvas width
    myXMargin = width() - myShapeWidth
    # to center the object, we would want to equal margin on either side
    # so its left offset would be half the total margin
    myXOffset = myXMargin/2
    # draw the rectangle
    # rect(x, y, width, height)
    rect(myXOffset, 0, width()/2, height()/2) # draw a big rectangle
saveImage('randomColors.gif') # save the file
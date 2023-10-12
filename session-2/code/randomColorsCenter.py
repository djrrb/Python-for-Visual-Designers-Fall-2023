for myNumber in range(10): # loop through 10 numbers
    newPage(500, 1000) # make a new page
    fill(random(), random(), random()) # set a random color
    myShapeWidth = width()/2
    myXMargin = width() - myShapeWidth
    myXOffset = myXMargin/2
    # rect(x, y, width, height)
    rect(myXOffset, 0, width()/2, height()/2) # draw a big rectangle
saveImage('randomColors.gif') # save the file
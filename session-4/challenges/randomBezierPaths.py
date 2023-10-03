# this is a shortcut function
# gets a random coorinate between zero and the document width
def getRandomCoords():
    # this uses the “return” keyword to return a value to the script
    return randint(0, width())

# loop through a number of frames
for frame in range(20):
    # set up the page and draw a background
    newPage()
    frameDuration(1/10)
    fill(0)
    rect(0, 0, width(), height())
    
    # each unique shape will have its own bezier path
    myPath = BezierPath()
    # we have to start a path by moving to certain coordinates
    myPath.moveTo((getRandomCoords(), getRandomCoords()))
    for myNumber in range(20):
        # now draw a bunch of curves 
        myPath.curveTo(
            (getRandomCoords(), getRandomCoords()), # handle 1
            (getRandomCoords(), getRandomCoords()), # handle 2
            (getRandomCoords(), getRandomCoords()) # handle 3
            )
    # set the color
    fill(1, 0, 1)
    # draw the path
    drawPath(myPath)

# save the resulting image
saveImage('randomBezierPaths.gif')

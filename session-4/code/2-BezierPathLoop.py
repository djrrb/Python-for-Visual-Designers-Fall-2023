# how tall to draw the first shape
# will reduce this every time
myShapeHeight = height()
# how many shapes to draw
myShapeCount = 8
# how long to draw the handle
myHandleLength = 100
# how much randomness should there be
myWobble = 250

# loop through the number of shapes to draw
for myShapeNumber in range(myShapeCount):
    # print the height of this shape
    print(myShapeHeight)
    # create a bezier path object
    myShape = BezierPath()
    # move to the bottom left
    myShape.moveTo((0, 0))
    # draw a line across the bottom
    myShape.lineTo((width(), 0))
    # draw a line up on the right
    myShape.lineTo((width(), myShapeHeight))
    # get two random wobble values
    # could be negative or positive
    myHandleWobble1 = randint(-myWobble, myWobble)
    myHandleWobble2 = randint(-myWobble, myWobble)
    # draw our big curve
    myShape.curveTo(
        (width(), myShapeHeight+myHandleLength+myHandleWobble1), # handle 1
        (0, myShapeHeight+myHandleLength+myHandleWobble2), # handle 2
        (0, myShapeHeight) # oncurve point
        )

    # set the fill color to random
    # with 30% opacity
    fill(random(), random(), random(), .3)
    # draw our shape
    drawPath(myShape)
    # augment the myShapeHeight variable
    # so the next shape will draw shorter than the last
    myShapeHeight -= height()/myShapeCount
    
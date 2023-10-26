# a simple shape
#oval(0, 0, 100, 100)
# a slightly more complex shape
#polygon((30, 50), (10, 210), (400, 310))
# and BezierPath() can handle our most complex shapes


myShapeHeight = 150 # how tall will the basic shape be
myHandleLength = 200 # how long to make the bezier handles

# define an empty BezierPath object
myShape = BezierPath()
# move to the starting point
myShape.moveTo((0, 0))
# draw a line across the bottom of the page
myShape.lineTo((width(), 0))
# draw a vertical line from the bottom right corner up
myShape.lineTo((width(), myShapeHeight))
# draw a curve from right to left
myShape.curveTo(
    (width(), myShapeHeight+myHandleLength), # handle 1
    (0, myShapeHeight+myHandleLength), # handle 2
    (0, myShapeHeight) # oncurve point
    )

# now that we are done drawing the shape
# we can draw it to the canvas
drawPath(myShape)

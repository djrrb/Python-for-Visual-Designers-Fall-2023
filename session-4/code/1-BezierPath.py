#oval(0, 0, 100, 100)

#polygon((30, 50), (10, 210), (400, 310))

#im = ImageObject()
myShapeHeight = 150
myHandleLength = 200

myShape = BezierPath()
myShape.moveTo((0, 0))
myShape.lineTo((width(), 0))
myShape.lineTo((width(), myShapeHeight))
myShape.curveTo(
    (width(), myShapeHeight+myHandleLength), # handle 1
    (0, myShapeHeight+myHandleLength), # handle 2
    (0, myShapeHeight) # oncurve point
    )

drawPath(myShape)

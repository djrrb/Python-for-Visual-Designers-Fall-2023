
myShapeHeight = height()
myHandleLength = 100

myShapeCount = 8
myWobble = 350

blendMode('screen')
for myShapeNumber in range(myShapeCount):
    print(myShapeHeight)
    myShape = BezierPath()
    myShape.moveTo((0, 0))
    myShape.lineTo((width(), 0))
    myShape.lineTo((width(), myShapeHeight))
    myHandleWobble1 = randint(-myWobble, myWobble)
    myHandleWobble2 = randint(-myWobble, myWobble)
    myShape.curveTo(
        (width(), myShapeHeight+myHandleLength+myHandleWobble1), # handle 1
        (0, myShapeHeight+myHandleLength+myHandleWobble2), # handle 2
        (0, myShapeHeight) # oncurve point
        )

    fill(random(), random(), random(), .5)
    drawPath(myShape)
    myShapeHeight -= height()/myShapeCount

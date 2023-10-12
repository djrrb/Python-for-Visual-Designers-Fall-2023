
myScaleValue = .9
myStrokeWidth = 5
myShapeSize = 1000-myStrokeWidth
translate(width()/2, height()/2)

stroke(1, 0, 0)
fill(None)
for myNumber in range(50):
    strokeWidth(myStrokeWidth)
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    scale(myScaleValue)
    print(myStrokeWidth)
    myStrokeWidth /= myScaleValue

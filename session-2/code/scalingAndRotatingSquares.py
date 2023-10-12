from colorsys import hsv_to_rgb

myHue = 0
mySat = 1
myVal = 1

mySquareCount = 50
myScaleValue = .9
myStrokeWidth = 5
myShapeSize = 1000-myStrokeWidth
translate(width()/2, height()/2)

stroke(None)
fill(None)

myToggle = True

for myNumber in range(mySquareCount):
    strokeWidth(myStrokeWidth)
    
    if myToggle:
        fill(0)
        myToggle = False
    else:
        print(hsv_to_rgb(myHue, mySat, myVal))
        fill(*hsv_to_rgb(myHue, mySat, myVal))
        myToggle = True
        
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    scale(myScaleValue)
    rotate(4)
    print(myStrokeWidth)
    myStrokeWidth /= myScaleValue
    myHue += 1 / mySquareCount
    print('myHue is', myHue)

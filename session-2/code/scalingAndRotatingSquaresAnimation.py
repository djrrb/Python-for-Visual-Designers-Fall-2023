from colorsys import hsv_to_rgb

myHue = 0
mySat = 1
myVal = 1

mySquareCount = 50
myFrameCount = 180
myScaleValue = .9
myStrokeWidth = 5
myRotateValue = 1
myShapeSize = 1000-myStrokeWidth


myToggle = True

for myFrameNumber in range(myFrameCount):
    newPage()
    translate(width()/2, height()/2)

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
        rotate(myRotateValue)
        print(myStrokeWidth)
        myStrokeWidth /= myScaleValue
        myHue += 1 / mySquareCount
        print('myHue is', myHue)
    
    myRotateValue += 360/myFrameCount
    
saveImage('rotatingSquares.gif')

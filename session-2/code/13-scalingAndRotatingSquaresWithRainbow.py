# we want to convert Hue/Saturation/Value to RGB
from colorsys import hsv_to_rgb

# set our starting hue, saturation, and value numbers
myHue = 0
mySat = 1
myVal = 1

mySquareCount = 50 # how many squares
myScaleValue = .9 # how much to scale by each time
myRotateValue = 4 # how much to rotate by each time
myShapeSize = width() # how big to draw our shape

# define a variable that we will use to toggle between True and False
myToggle = True

# move to center of canvas
translate(width()/2, height()/2)

for myNumber in range(mySquareCount):
    
    # if myToggle is True, run this code block and set myToggle to False
    if myToggle:
        fill(0)
        myToggle = False
    # if myToggle is not True, run this code block instead and set myToggle to True
    else:
        print(hsv_to_rgb(myHue, mySat, myVal))
        fill(*hsv_to_rgb(myHue, mySat, myVal))
        myToggle = True
        
    # draw a centered rectangle
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    
    # scale the canvas
    scale(myScaleValue)
    # rotate the canvas
    rotate(myRotateValue)
    
    # augment the hue by one fraction of the total loop
    myHue += 1 / mySquareCount
    print('myHue is', myHue)

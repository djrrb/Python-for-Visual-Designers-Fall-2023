# import the hue/saturation/value converter from the colorsys library
from colorsys import hsv_to_rgb

# set our initial hue/saturation/value numbers
myHue = 0 # red
mySat = 1 # full brilliance
myVal = 1 # full brightness

mySquareCount = 30 # how many shapes to draw
myFrameCount = 90 # how many frames to draw
myScaleValue = .9 # how much to scale by each time
myRotateValue = 1 # how much to rotate by each time (this will change)
# our starting shape size
myShapeSize = 1000
# our toggle variable, will alternate between True and False
myToggle = True

# loop through our frames
for myFrameNumber in range(myFrameCount):
    # code at this indent will run once per frame
    # make a new page
    newPage()
    # move to the center of the page
    translate(width()/2, height()/2)

    # loop through our shapes
    for myNumber in range(mySquareCount):
        # code at this indent will run once per shape per page

        # if myToggle is True, set the fill to black
        # also set myToggle to false, so it will be different next time    
        if myToggle:
            fill(0)
            myToggle = False
        # if myToggle is False, set the fill to our HSV color
        # we must convert it to RGB first, since that's what fill() wants
        # and we must use '*' to unpack the 3 red, green, blue values
        # and feed them to fill() separately rather than as a single tuple
        else:
            print('converted to rgb:', hsv_to_rgb(myHue, mySat, myVal))
            fill(*hsv_to_rgb(myHue, mySat, myVal))
            myToggle = True
            
        # draw our cnetered rectangle
        rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
        # scale the canvas down
        scale(myScaleValue)
        # rotate the canvas
        rotate(myRotateValue)
    
        # each time we draw a shape, augment the hue
        # by setting it to 1/mySquareCount, the value will increase by 1 over the course of the total loop
        myHue += 1 / mySquareCount
        print('myHue is', myHue)

    # dedent, this code only runs once per frame again
    # set the rotate value so that it will rotate in a circle over the course of the animation (360° is full circle)    
    myRotateValue += 360/myFrameCount
    
# save the image as a gif
saveImage('rotatingSquares.gif')

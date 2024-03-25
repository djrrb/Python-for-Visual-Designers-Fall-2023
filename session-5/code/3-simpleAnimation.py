# how many shapes
myShapeCount = 10
# how big
myShapeSize = 100
# how many frames to animate
myFrameCount = 10

# loop through each frame
for myFrameNumber in range(myFrameCount):
    # make a new page
    # if we comment out the new page
    # all frames will be drawn on the same page
    newPage()
    # loop through each shape
    for myShapeNumber in range(myShapeCount):
        # if our shape corresponds to the frame, draw it
        # otherwise skip it
        if myFrameNumber == myShapeNumber:
            # move our x value across the page
            myX = myShapeNumber*myShapeSize
            # make y constant
            myY = 0
            # draw the oval
            oval(myX, myY, myShapeSize, myShapeSize)
        
saveImage('simpleAnimation.gif')
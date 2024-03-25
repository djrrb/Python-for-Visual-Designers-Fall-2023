# how many shapes to draw
myShapeCount = 50
# how big to make each shape
myShapeSize = width()/myShapeCount
# draw one frame for every shape
myFrameCount = myShapeCount

# loop through frames
for myFrameNumber in range(myFrameCount):
    # new page and background for each frame
    newPage()
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    # change the frame duration for a smother animation
    frameDuration(1/24)
    
    # move to the vertical center of the page
    # so our waveform can go both above and below
    translate(0, height()/2)

    # loop through each shape
    for myShapeNumber in range(myShapeCount):
        # only draw the shape that corresponds
        # to our current frame
        if myShapeNumber == myFrameNumber:
            # determine how far we are through the animation
            myProgress = myShapeNumber / myShapeCount
            # get our position on a circle (2*pi)
            # using the sine function
            myCurvature = sin(2*pi*myProgress)
            # how tall to make each wave (half the canvas)
            myWaveSize = height()/2
            # get our y position by multiplying our circle position by the amplitude of our wave
            myY = myCurvature*myWaveSize
            # get our x position by moving across the page
            # from left to right
            myX = myShapeNumber*myShapeSize
            # (or if we want we can set a single x position
            # to have it bounce up and down like a ball)
            #myX = width()/2
            #draw our oval to canvas
            oval(myX, myY, myShapeSize, myShapeSize)
        
saveImage('sineWave.gif')
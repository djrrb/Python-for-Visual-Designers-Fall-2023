myImageName = 'Juvenile_Ragdoll.jpg'
myXCount, myYCount = 10, 10
myFrameCount = 10
myMultiplier = .2

# phase 1 will enhance resolution , phase 2 will degrade
for myPhase in range(2):
    # now loop through each frame
    for myFrameNumber in range(myFrameCount):

        # define the image
        myImage = ImageObject(myImageName)
        # make the page at the dimensions
        newPage(*myImage.size())
        # get the dimensions of each cell
        myCellWidth, myCellHeight = width()/myXCount, height()/myYCount

        # loop through rows
        for myYNumber in range(myYCount):
            # loop through columns
            for myXNumber in range(myXCount):
                # get x and y coordinates of each shape
                myX = myCellWidth * myXNumber
                myY = myCellHeight * myYNumber
                # eyedrop color at those coordinates
                myColor = imagePixelColor(myImage, (myX, myY))
                # set fill to our eyedropped color
                # unpacking r,g,b,a and feeding them to fill() separately
                fill(*myColor)
                # draw a rectangle
                rect(myX, myY, myCellWidth, myCellHeight)
            
                # this code runs once per column per row per frame per phase
            # this code runs once per row per frame per phase
        # this code runs once per frame per phase
        myXCount = int(myXCount + myXCount*myMultiplier)
        myYCount = int(myYCount + myYCount*myMultiplier) 

    # this runs once per phase
    myMultiplier = -myMultiplier
    
    # if we are at the end of the first phase
    if myPhase == 0:
        # make a frame where we see the full res image
        newPage(*myImage.size())
        frameDuration(1)
        image(myImage, (0, 0))
    
# this code runs once
saveImage('resolution2.gif')
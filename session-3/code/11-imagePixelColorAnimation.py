myImageName = 'Juvenile_Ragdoll.jpg'
myXCount, myYCount = 10, 10
myFrameCount = 10
myMultiplier = .2

for myPhase in range(2):
    for myFrameNumber in range(myFrameCount):

        myImage = ImageObject(myImageName)

        newPage(*myImage.size())

        myCellWidth, myCellHeight = width()/myXCount, height()/myYCount

        for myYNumber in range(myYCount):
            for myXNumber in range(myXCount):
                myX = myCellWidth * myXNumber
                myY = myCellHeight * myYNumber
                myColor = imagePixelColor(myImage, (myX, myY))
                fill(*myColor)
                rect(myX, myY, myCellWidth, myCellHeight)
            
                # this code runs once per column per row per frame
            # this code runs once per row per frame
        # this code runs once per frame
        myXCount = int(myXCount + myXCount*myMultiplier)
        myYCount = int(myYCount + myYCount*myMultiplier) 

    # this runs once per phase
    myMultiplier = -myMultiplier
    
    if myPhase == 0:
        newPage(*myImage.size())
        frameDuration(1)
        image(myImage, (0, 0))
    
# this code runs once
saveImage('resolution2.gif')
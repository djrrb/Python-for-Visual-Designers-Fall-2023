myShapeCount = 10
myShapeSize = 100
myFrameCount = 10

for myFrameNumber in range(myFrameCount):
    newPage()
    for myShapeNumber in range(myShapeCount):
        if myFrameNumber == myShapeNumber:
            myX = myShapeNumber*myShapeSize
            myY = 0
            oval(myX, myY, myShapeSize, myShapeSize)
        
saveImage('moveAcrossPage.gif')
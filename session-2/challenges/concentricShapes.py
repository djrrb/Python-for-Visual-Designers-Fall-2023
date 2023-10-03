# set a number of frames
myFrames = 5
myShapeSize = width()*2

# loop through each frame
for myFrame in range(myFrames):
    # make a new page
    newPage()
    # make a background
    rect(0, 0, width(), height())
    translate(width()/2, height()/2)
    
    for myShape in range(50):
        
        if myShape % 2:
            fill(random(), random(), random())
        else:
            fill(1)
        oval(
            -myShapeSize/2, 
            -myShapeSize/2, 
            myShapeSize, 
            myShapeSize
        )
        scale(.9)
        
    
saveImage('concentricShapes.gif')
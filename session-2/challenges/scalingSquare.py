# make a growing square in black and white
# determine the initial size of the square
# this variable will grow for each frame
myShapeSize = 100
# how many frames should the square grow for
myFramesPerPhase = 18

# define a foreground and background color
# these will flip at the end of the first phase
fgColor = 1, 1, 1
bgColor = 0, 0, 0

# this animation has two phases
# one with a black square, one with a white square
# so we can do a loop through each phase to avoid copy/pasting the code
for myPhase in range(2):
    # myPhase = 0, 1
    # now loop through 
    for myFrame in range(myFramesPerPhase):
        # myFrame = 0, 1, 2, 3...
        # make our new page
        newPage()
        frameDuration(1/15)
        
        # draw a background
        fill(*bgColor)
        rect(0, 0, width(), height())
        
        #move to the center
        translate(width()/2, height()/2)
        # use the foreground color and draw the rectangle
        fill(*fgColor)
        rect(
            -myShapeSize/2, 
            -myShapeSize/2,
            myShapeSize,
            myShapeSize
        )
        # for every frame, make the square a little bigger
        myShapeSize = myShapeSize + 50

    # at the end of the first phase
    # make the foreground color the background color
    # and vice versa
    fgColor = 0, 0, 0
    bgColor = 1, 1, 1
    # also reset the shape size so it’s small again
    myShapeSize = 100
 
# save it! 
saveImage('scalingSquare.gif')
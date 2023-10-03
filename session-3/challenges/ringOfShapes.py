# make a function that draws a simple triangle
def drawTriangleFromCenter(theShapeSize):
    # a triangle is a three point polygon
    polygon(
        (-theShapeSize/2, 0), # the lower left point is half the shape width to the left
        (theShapeSize/2, 0), # the lower right point is half the shape width to the right
        (0, theShapeSize), # the top point is the full shape width up
        )

# make a function that draws a ring of shapes
def drawRing(theShapeCount=10, theShapeSize=100, theOffset=10):
    with savedState():
        for theShape in range(theShapeCount):
            with savedState():
                translate(0, theOffset)
                drawTriangleFromCenter(theShapeSize)
            rotate(360/theShapeCount)

####
####
####
# set some variables

# the radius of the ring
myOffset = 10
myShapeCount = 6
myShapeSize = 5
myRingCount = 50

# set some variable for our document

# now let's draw our document
newPage()

# draw a background
fill(1)
rect(0, 0, width(), height())

# move to the center of the document
translate(width()/2, height()/2)

# add a shadow to all shapes
shadow((-2, 2), 5, (0, 0, 0, .1))

# loop through the number of rings we want to draw
for myRing in range(myRingCount):
    # make each ring a different color
    fill(random(), random(), random())
    # draw our ring of shapes
    drawRing(myShapeCount, myShapeSize, myOffset)
    # now augment our variables so the next ring will be drawn differently
    # with more shapes
    myShapeCount += 3
    # with a slightly bigger size
    myShapeSize += 2
    # make the offset bigger so each ring is drawn larger
    myOffset += myShapeSize
    
saveImage('ringOfShapes.png')
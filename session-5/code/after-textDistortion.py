# import pens that we will use to filter the shapes
from fontTools.pens.recordingPen import RecordingPen
from fontPens.flattenPen import FlattenPen

# make a lower left margin
translate(50, 50)

# how much wiggle do we want to add to the letters
myWiggle = 5
# how long should the segments be on each shape
mySegmentLength = 13

# create a formatted string
myString = FormattedString('Hello!', font='ComicSansMS', fontSize=300)

# create a path
myShape = BezierPath()
# feed our string into our path to convert text to path
# like "create outlines" in illustrator
myShape.text(myString)

# draw the text as a shape in red
fill(1, 0, 0)
drawPath(myShape)

# move up
translate(0, 300)

# make a second path to convert our shape to a bunch of short straight lines
myFlattenedShape = BezierPath()
# create a flatten pen that will redraw an outline as many straight segments
myFlattenPen = FlattenPen(
    myFlattenedShape, # the shape to draw TO
    approximateSegmentLength=mySegmentLength, # 
    segmentLines=True
)
# draw our first shape into our pen
# this will create the outlines in our second shape "myFlattenedShape"
myShape.drawToPen(myFlattenPen)

# draw a green flattened shape to canvas
# this shape no longer has any curves, but many short straight segments
fill(0, 1, 0)
stroke(None)
drawPath(myFlattenedShape)

# move up
translate(0, 300)

# now let’s add randomness to the position of those points


# first let’s record the list of moveTo, lineTo, and curveTo commands
# from our flattened shape
# then we can "replay" those but distort the points
myRecordingPen = RecordingPen()
# draw our flattened shape to the recording pen
myFlattenedShape.drawToPen(myRecordingPen)

# let’s create a third shape that will contain our distorted outline
myDistortedShape = BezierPath()

# this will loop through the moveTo, lineTo, curveTo commands
# needed to draw the recorded shape
for myCommand, myPoints in myRecordingPen.value:    
    # make a list where we will collect new (x, y) points
    # that are randomized from the existing points
    newPoints = []
    # loop through each point in the command
    # lines will have one endpoint
    # curves will have two handle points and one endpoint
    for myPoint in myPoints:
        # split our point into x and y
        myX, myY = myPoint
        # augment our points with an element of randomness
        # that is governed by myWiggle
        myX += randint(-myWiggle, myWiggle)
        myY += randint(-myWiggle, myWiggle)
        # append our points to our new points list
        newPoints.append((myX, myY))
    # use the getattr() function to get the attribute from our shape object
    # if myCommand is "lineTo", this is like running
    # myDistortedShape.lineTo(*newPoints)
    getattr(myDistortedShape, myCommand)(*newPoints)

# draw our distorted path to canvas in black
fill(0)
drawPath(myDistortedShape)

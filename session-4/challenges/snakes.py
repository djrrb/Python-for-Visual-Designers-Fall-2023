# how many frames to draw
frames = 1

maxWiggle = 100 # how much should things wiggle
snakeCount = 15 # how many lines to draw
segmentLength = 200 # how long each segment might be
thickness = 20 # stroke thickness
drawPoints = False # do we want to see the bezier points

# set the length of our handles
# we could use more advanced math for this
# or just make up a number, shorter handles are more jagged
# longer handles are more squarish
handleLength = segmentLength * .5


# make the column width equal to the total width divided by the number of snakes
columnWidth = width()/snakeCount

# define a bottom and top margin
margin = 0


# okay let’s draw

for frame in range(frames):
    newPage()

    # draw a background
    rect(0, 0, width(), height())

    # give us a bottom margin
    translate(columnWidth/2, margin)
    
    # draw lines, with the bottoms spaced equidistantly
    for i in range(snakeCount):

        snake = BezierPath()
        snake.moveTo((0, 0))
        # keep track of our previous point
        # this way we can draw a handle relative to it
        prevY = 0
        prevX = 0
        # since our first point was at zero, we will start drawing new points segmentLength units from there, and keep on going by segmentLengths
        for y in range(segmentLength, height()-margin*2+segmentLength, segmentLength):
            # get an x value for our point somewhere between -100 and 100
            x = randint(-maxWiggle, maxWiggle)
            snake.curveTo(
                (prevX, prevY+handleLength), # the first handle, drawn one handleLength above the previous point
                (x, y-handleLength), # the second handle, drawn one handleLength below our new point
                (x, y) # finally, our new point
            )
            # augment our previous point so it’s ready for next time
            prevX = x
            prevY = y
    

        # we’re prepared our bezier curve
        # now let’s set the color and draw it 
        fill(None)
        stroke(random(), random(), random())
        lineCap('round')
        strokeWidth(thickness)
        drawPath(snake)
    
        # check the drawPoints variable to determine if we will also draw the points
        # if so, we can loop through each contour in the BezierPath(), each segment within that contour, and each point within that segment. We can keep track of the previous point in order to attach a handle to it. It’s all a bit annoying, but just showing you it’s possible.
        if drawPoints:
            # this is a little hacky but I know we always start at (0, 0)
            prevPoint = (0, 0)
            for contour in snake:
                for segment in contour:
                    for point in segment:
                        # each point is an (x, y) tuple
                        # point[0] is x
                        # point[1] is y
                        fill(1)
                        stroke(None)
                        oval(point[0]-5, point[1]-5, 10, 10)
                    # if our segment has a length of three
                    # we can assume that the first two are handles
                    # and the third is the oncurve points
                    if len(segment) == 3:
                        stroke(1)
                        strokeWidth(1)
                        # draw a line to a previous point
                        line(segment[0], prevPoint)
                        # draw a line to the following point 
                        line(segment[1], segment[2])
                        # keep track of our previous point
                        prevPoint = segment[2]

        # now that we’re all done 
        # move to the next column
        translate(columnWidth)
    
#saveImage('snakes.gif')
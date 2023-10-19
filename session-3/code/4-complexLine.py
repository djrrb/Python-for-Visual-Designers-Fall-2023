# how many lines to draw
myLineCount = 250

# how far will we draw from the edge (can be negative)
myMargin = 50 

# round the edge of each line
lineCap('round')

# draw our margin space one time
# set the fill color
fill(.9)
rect(
    myMargin, # offset left margin
    myMargin, # offset bottom margin
    width()-myMargin*2, # full width of canvas minus two margins
    height()-myMargin*2 # full height of canvas minus two margins
)

# loop through our line count
for myLineNumber in range(myLineCount):
    # set the stroke to a random color
    stroke(random(), random(), random())
    # set the stroke width
    strokeWidth(10)
    
    # randomly calculate 4 coordinates
    # the start (x, y) and the end (x, y)
    # use randint() and go between our margin and the canvas size minus our margin
    myStartX = randint(myMargin, width()-myMargin)
    myStartY = randint(myMargin, height()-myMargin)
    myEndX = randint(myMargin, width()-myMargin)
    myEndY = randint(myMargin, height()-myMargin)
    
    # draw the line
    # line((x1, y1), (x2, y2))
    line((myStartX, myStartY), (myEndX, myEndY))

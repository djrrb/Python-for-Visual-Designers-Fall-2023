# make a center oval function that only requires a width and height
def centerOval(myW, myH):
    oval(-myW/2, -myH/2, myW, myH)

# set some variables
myRowCount = 10 # number of rows
myColCount = 10 # number of cols
myColWidth = width()/myRowCount # width of each col
myRowHeight = height()/myRowCount # width of each row
myBasicShapeSize = myColWidth*.75 # drw the shape at 3/4 the grid size, give or take
mySizeVariation = myBasicShapeSize // 10 # vary each shape randomly by 10%
# use two divide symbols so the result is an integer, which is required by the randint() function


# make a pink background
fill(1, 0, 1)
rect(0, 0, width(), height())

# set the fill color to black
fill(0)

# move to the center of each grid cell
translate(myColWidth/2, myRowHeight/2)


# loop through rows
for myRowNumber in range(myRowCount):
    # save the state
    with savedState():
        for myColNumber in range(myColCount):
            # get a number between -mySizeVariation and mySizeVariation
            myVariationAmount = randint(-mySizeVariation, mySizeVariation)
            # get the size from the basic size and random variation
            myShapeSize = myBasicShapeSize + myVariationAmount
            # draw the oval
            centerOval(myShapeSize, myShapeSize)
            # move to the right
            translate(myColWidth)
        # exit col loop
    # exit saved state
    # move up for each column
    translate(0, myRowHeight)
# exit all loops
saveImage('polkaDotPattern.png')
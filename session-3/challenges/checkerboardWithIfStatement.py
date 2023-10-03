# make a checkerboard
myRows = 10
myCols = 10

newPage()

# calculate the grid size
myGridSize = width()/myRows

# loop through rows and columns to make a grid
for myRow in range(myRows):
    # save our state before we translate so we can always return to the left
    with savedState():
        for myCol in range(myCols):
            # if the column number and row number are both odd, fill black
            if  myCol % 2 and myRow % 2:
                fill(0)
            # if the column number and row number are both even, fill black
            elif not myCol % 2 and not myRow % 2:
                fill(0)
            # in all other cases, fill white
            else:
                fill(1)
            # draw a rectangle
            rect(0, 0, myGridSize, myGridSize)
            # move to the right
            translate(myGridSize, 0)
        # exit the saved state and return to the left
    # move up
    translate(0, myGridSize)

# save image
saveImage('checkerboard.png')
# make a grid using translate() and savedState()

# how many columns and rows to draw
myCols = 10
myRows = 10

# determine the width and height of each column
# based on the canvas and amount of rows/cols
myColWidth = width()/myCols
myRowHeight = height()/myCols

# draw a background if we want
# just a rectangle that fills the canvas
rect(0, 0, width(), height())

# loop through each row
for myRow in range(myRows):
    # save our state
    # this will allow us to easily move back 
    # to the left side of the canvas by dedenting
    # when we are done with each column
    with savedState():
        # now loop through the columns
        for myCol in range(myCols):
            # set a random color
            fill(random(), random(), random())
            # draw a rectangle or oval
            # random() is a number between 0 and 1
            # 50% chance it is less than .5
            # an easy way to do a coin toss
            if random() < .5:
                rect(0, 0, myColWidth, myRowHeight)
            else:
                oval(0, 0, myColWidth, myRowHeight)
            # move us to the right
            translate(myColWidth, 0)
        # now we dedent twice
        # once to end the loop
        # and once to go back to the saved state
        # now we are drawing from the left of the canvas again
        # and can move up on the canvas to draw the next row
    translate(0, myRowHeight)
    
# dedent again to save once
saveImage('grid.png')
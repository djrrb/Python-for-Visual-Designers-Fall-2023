# draw a brick wll

# set our main variables
# how tall should each brick be
myBrickHeight = 60
# set each brick to be 3x wider than it is tall
myBrickWidth = 3 * myBrickHeight
myMortarThickness = 3

# caculate how many bricks to draw automatically in order to fill the space
# divide canvas height by brick height, and round up
myRows = ceil(height() / myBrickHeight)
# divide canvas width by brick width, and round up
myCols = ceil(width() / myBrickWidth)+1

# set the stroke width and fill color
strokeWidth(myMortarThickness)
stroke(.8, .8, .6)


# loop through each row
for i in range(myRows):
    # save our current state!
    with savedState():
        # if it’s an odd row, move us one half-brick to the left
        if i % 2:
            translate(-myBrickWidth/2)
        # loop through each column
        for col in range(myCols):
            # set the fill color
            # right now it’s a 50/50 chance lighter vs darker red
            if random() < .5:
                fill(.5, 0, 0)
            else:
                fill(.6, 0, 0)
            # draw the rectangle
            rect(0, 0, myBrickWidth, myBrickHeight)
            # move to the right to draw the next rectanle
            translate(myBrickWidth)
    # at the end of each row
    # move up to draw the next row
    translate(0, myBrickHeight)

saveImage('bricks.png')
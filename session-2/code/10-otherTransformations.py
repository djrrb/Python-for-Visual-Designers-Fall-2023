# set a shape size
myShapeSize = 800

# move (0, 0) to the middle of the canvas
translate(width()/2, height()/2)
# rotate the canvas (degrees)
rotate(45)
# skew the canvas
skew(10)
# scale the canvas (1 = 100%)
# can take 1 number (x and y) or separate x and y values
scale(.5, 1)

# draw a centered rectangle
rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)

# set the fill color to green
fill(0, 1, 0)
# make the font bigger
fontSize(100)
# set some text to show the skew
text('hello world', (0, 0))
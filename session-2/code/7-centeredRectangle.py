# set a variable to control the size of our shape
myShapeSize = 500

# move to the center of the page
translate(width()/2, height()/2)

# since drawbot draws from the bottom left
# we have to offset the shape to the left and down
# by half its width and height

# rect(x, y, width, height)
rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
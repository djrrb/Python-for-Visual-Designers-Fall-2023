mySquareCount = 50 # how many squares to draw
myScaleValue = .9 # how much to scale by each time
myRotateValue = 4 # how much to rotate by each time
myShapeSize = width() # how big to draw the first square

# move to the center of the canvas
translate(width()/2, height()/2)

# loop through our range of numbers between 0 and 50
for myNumber in range(mySquareCount):
    # set the fill color to random
    fill(random(), random(), random()) 
    # draw a centered rectangle
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    # scale by our scale value
    scale(myScaleValue)
    # rotate by 4 
    rotate(myRotateValue)

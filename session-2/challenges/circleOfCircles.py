# set the blend mode to overlay
# this will let the shapes overlap
blendMode('overlay')

# set up some variables
myShapeSize = 250 # how big each circle is
myRadius = 250 # the 
myShapeCount = 15 # how many shapes to draw

# move to the center
translate(width()/2, height()/2)

# loop through the number of shapes we will draw
for myShape in range(myShapeCount):
    # make a random fill
    fill(random(), random(), random())
    # draw the shape
    # the x and y will be minus half the shape size
    # BUT the y will also be offset by myRadius
    # this way, when I rotate the canvas, they will always be a certain distance from the center
    oval(
        -myShapeSize/2, # x
        -myShapeSize/2+myRadius, # y
        myShapeSize, # width
        myShapeSize # height
    ) 
    # rotate by a certain amount
    # 360/myShapeCount will create a complete rotation
    rotate(360/myShapeCount)
    
saveImage('circleOfCircles.png')
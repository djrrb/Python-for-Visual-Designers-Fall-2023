# make some confetti

newPage()


# how many shapes to draw
myShapeCount = 2000
# how big should each shape be
myShapeSize = 25
# since drawbot draws from the lower left, if we want the circle to be centered on the (x, y) we can offset it by 
# this is a little confusing, we will talk about it next time
myShapeOffset = myShapeSize/2

# loop through the range between 0 and myShapeCount, creating the variable myShape in the process
for myShape in range(myShapeCount):
    # fill with a random color
    fill(random(), random(), random())
    # set the X and Y variables as 
    # random() is a number between 0 and 1
    # so if we multiply that by the width and height, we get a random coordinate on the canvas
    myX = random()*width()
    myY = random()*height()
    # draw the oval
    oval(
        myX-myShapeOffset, # x position, minus the offset
        myY-myShapeOffset, # y position, minus the offset
        myShapeSize, # width
        myShapeSize # heiht
        )

saveImage('confetti.png')
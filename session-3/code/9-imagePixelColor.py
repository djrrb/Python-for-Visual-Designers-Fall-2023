# create a low-res vector interpretation of an image

# what's the image filename
myImageName = 'Juvenile_Ragdoll.jpg'
# make an image object
myImage = ImageObject(myImageName)
# make a new page the size of the image
# but don’t draw the image
newPage(*myImage.size())

# make a grid
myXCount, myYCount = 28, 25
# calculate the cell dimensions based on
# canvas size and row/col count
myCellWidth, myCellHeight = width()/myXCount, height()/myYCount

# loop through each row
for myYNumber in range(myYCount):
    # loop through each column
    for myXNumber in range(myXCount):
        # get our x and y values by multiplying the 
        # column/row number by the cell size
        myX = myCellWidth * myXNumber
        myY = myCellHeight * myYNumber
        # get the color by eyeDropping the X, Y coordinates
        myColor = imagePixelColor(myImage, (myX, myY))
        # set the fill color to our eyedropped variable
        # unpack the r,g,b,a values and feed them to fill()
        # separately
        fill(*myColor)
        # draw an oval
        oval(myX, myY, myCellWidth, myCellHeight)
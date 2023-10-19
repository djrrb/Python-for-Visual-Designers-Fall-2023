myImageName = 'Juvenile_Ragdoll.jpg'

myImage = ImageObject(myImageName)

newPage(*myImage.size())
#image(myImage, (0, 0))

#print(imagePixelColor(myImage, (0, 0)))

#fill(*imagePixelColor(myImage, (600, 640)))

myXCount, myYCount = 35, 42
myCellWidth, myCellHeight = width()/myXCount, height()/myYCount

for myYNumber in range(myYCount):
    for myXNumber in range(myXCount):
        myX = myCellWidth * myXNumber
        myY = myCellHeight * myYNumber
        myColor = imagePixelColor(myImage, (myX, myY))
        fill(*myColor)
        rect(myX, myY, myCellWidth, myCellHeight)
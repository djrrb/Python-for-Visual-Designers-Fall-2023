myImageName = 'black-raspberries.jpg'

myImage = ImageObject(myImageName)
print(myImage)
print(myImage.size())
newPage(*myImage.size())
image(myImage, (0, 0))

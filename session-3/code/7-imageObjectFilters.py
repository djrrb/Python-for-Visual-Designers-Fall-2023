myImageName = 'Juvenile_Ragdoll.jpg'

myImage = ImageObject(myImageName)
print(myImage)
print(myImage.size())

#myImage.sepiaTone(0)
#myImage.vignette(100, 10)
myImage.kaleidoscope(9)

newPage(*myImage.size())
image(myImage, (0, 0))

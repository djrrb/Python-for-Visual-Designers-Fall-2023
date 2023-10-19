# set our filename
myImageName = 'Juvenile_Ragdoll.jpg'

# create an image object that we can manipulate
# before drawing to the canvas
myImage = ImageObject(myImageName)

# use some methods
# https://drawbot.com/content/image/imageObject.html

#myImage.sepiaTone(0)
#myImage.vignette(100, 10)
myImage.kaleidoscope(9)

# set the canvas as the image size, unpacking the width and height
newPage(*myImage.size())
# draw the modified image to canvas
image(myImage, (0, 0))

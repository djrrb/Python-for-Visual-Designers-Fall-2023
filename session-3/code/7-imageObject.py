# set the filename as a variable
myImageName = 'black-raspberries.jpg'

# define an image object using the filename
# but don’t draw it to canvas (yet!)
myImage = ImageObject(myImageName)

# see that our image exists as an object, even if we
# don’t see it on canvas
print(myImage)

# print the image dimensions
print(myImage.size())

# set the canvas size to the image dimensions
# use * to unpack the width and height
# and pass them to newPage() as separate values
newPage(*myImage.size())

# now that we have set the canvas as the correct size
# we can draw the image object to canvas
image(myImage, (0, 0))

# set the image filename
myImageName = 'Juvenile_Ragdoll.jpg'
# load the image but don’t draw it to canvas
myImage = ImageObject(myImageName)

# make a new page the size of the canvas
newPage(*myImage.size())
# draw the image to the canvas
image(myImage, (0, 0))

# use imagePixelColor to eyedrop the image
# and get the color of a particular pixel
# the function takes the imageObject and the (x, y) coordinates
print(imagePixelColor(myImage, (500, 500)))

# set the fill color
# unpack the r, g, b, a elements from the tuple
# and pass them to fill separately
fill(*imagePixelColor(myImage, (500, 500)))
stroke(1)
strokeWidth(10)
# draw a rectangle so we can see the color at (500, 500)
# it’s blue, from the blanket
rect(100, 100, 200, 200)

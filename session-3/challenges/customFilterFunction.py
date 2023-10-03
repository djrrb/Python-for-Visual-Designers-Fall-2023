# make a custom function that takes one argument, an image to process
def myCustomFilter(myImageToProcess):
    # inside this funtion myImageToProcess is a variable that equals the argument
    
    # get the size of the image to process, we will use it to calculate the center
    myWidth, myHeight = myImageToProcess.size()
    # get the center point of the image
    myCenter = (myWidth/2, myHeight/2)
    # invert the colors
    myImageToProcess.colorInvert()
    # posterize the image
    myImageToProcess.colorPosterize(3)
    # do a twirl distorition located at the center which occupies 1/3 of the image
    myImageToProcess.twirlDistortion(myCenter, width()/3)

# now we have dedented, ending the function

# make an image object from a file
myImage = ImageObject('image.jpg') 
# pass the image object to our filter, which will modify it
myCustomFilter(myImage)            
# make a new page
newPage(*myImage.size()) 
# draw the image
image(myImage, (0, 0))    

# save the image
saveImage('customFilterFunction.jpg')          
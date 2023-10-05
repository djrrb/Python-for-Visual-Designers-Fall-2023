# set a string variable
myString = 'the quick brown fox'

# loop through a range of then numbers 
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for myPage in range(0, 10):
    # myPage will be equal to the number of our current page
    # starting at 0 and going to 9
    # print the current page number
    print(myPage)
    # make a new page
    newPage('Letter')
    # set the frame rate
    # 1 = 1 second
    # 1/12 = 12 frames per second
    frameDuration(1/12)
    
    # draw a rectangle the full size of the canvas
    # rect(x, y, width, height)
    # 0, 0 represents the bottom left of the canvas
    # width() and height() are functions that give us
    # the full dimensions of the canvas
    rect(0, 0, width(), height())
    
    # loop through each letter in our string
    for myLetter in myString:
        # define a variable with a random horizontal position on the canvas
        # get a random number between 0 and the canvas width
        myX = randint(0, width())
        # do the same for height
        myY = randint(0, height())
        
        # set the font size
        fontSize(130)
        
        # random() gives us a random number between 0 and 1
        # we can call it three times to get three random numbers 
        # for red, green, and blue values
        # set the fill color to be random
        fill(random(), random(), random())
        
        # draw our text to the canvas as the random position
        text(myLetter, (myX, myY))
        
    # if we want to save each frame as a PDF, we can have 
    # the saveImage() function indented and then include
    # the page number in the filename
    # since the page number is an integer, we have to use str()
    # to convert it to a string
    #saveImage('myImage'+str(myPage)+'.png')
    
# save the whole thing as an animated gif
# this will go in the same folder as the script
saveImage('myImage.gif')
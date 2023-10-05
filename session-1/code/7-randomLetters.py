# set a string variable
myString = 'the quick brown fox'

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
    
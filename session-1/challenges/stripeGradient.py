# make a new page
newPage(1000, 1000)
# could also give it a size
#newPage('Letter')

# define my starting coordinates
myX = 0
myY = 0
# how many stripes do we want to draw
myCols = 10
# how wide is each stripe?
# calculate it by dividing the full width of the canvas by the number of columns
myWidth = width()/myCols

# how tall is each stripe? the full height of the canvas
myHeight = height()

myRed = 1
myGreen = 0
myBlue = 0

# now let’s draw each stripe in a loop
# range(myCols) is a sequence that will give us as many numbers as there are between 0 and myCols
# myItem is a new variable created by our loop, set to the current item in the sequence
for myItem in range(myCols):
    # set the fill color to my color variables
    fill(myRed, myGreen, myBlue)
    # print our x coordinate so we can keep track of where we are
    print(myX)
    # draw the rectangle to the canvas
    rect(myX, myY, myWidth, myHeight)
    # augment myX by 100 each time
    # this is important because otherwise we will draw all the stripes in the same place!
    myX += myWidth
    # also augment the amount of green each time we draw a rectangle
    myGreen += 1/myCols
    
# if we want to save this
saveImage('stripeGradient.png')
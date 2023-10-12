for myFrame in range(5):
    newPage()
    myX = 0
    # loop through 10 numbers
    for myNumber in range(10):
        # draw a rectangle 50 points wide and the full height of the canvas
        # set the x position to the myX variable
        # rect(x, y, width, height)
        fill(random(), random(), random())
        rect(myX, 0, 50, height())
    
        # augment myX by adding 100 to it every time
        # this means the rectangles will shift to the right each time
        # creating stripes
        myX = myX + 100 # x += 50

saveImage('funStripes.gif')
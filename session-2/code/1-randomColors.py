# animate through some colors
# range(10) is a sequence of 10 numbers:
#     0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# loop through it
for myNumber in range(10):
    # print the current number
    print(myNumber)
    # make a new page
    newPage()
    # set the fill color to random
    fill(random(), random(), random())
    # draw a rectangle starting at (0, 0) 
    # and filling the full width and height of the canvas
    rect(0, 0, width(), height())
# dedent so that we exit the loop
# and only save the file once
saveImage('randomColors.gif')
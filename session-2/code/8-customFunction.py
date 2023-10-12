# create a custom function that will center a rectangle
# this function will take a required width (myW) and height (myH)
def myCenteredRect(myW, myH):
    print('this is a centered rectangle', myW, myH)
    # since drawbot draws from the lower left
    # to center it, we will shift it left and down by half its dimensions
    rect(-myW/2, -myH/2, myW, myH)
    
print(myCenteredRect)

# move to the center of the page
translate(width()/2, height()/2)

# draw a centered rectangle
myCenteredRect(500, 500)

# set the fill color to red
fill(1, 0, 0)
# draw another centered rectangle on top
myCenteredRect(250, 100)
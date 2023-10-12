def myCenteredRect(myW, myH):
    print('this is a centered rectangle', myW, myH)
    rect(-myW/2, -myH/2, myW, myH)

# with savedState() will save the canvas setting at this moment in time
with savedState():
    # within our savedState, we can make further changes to the canvas
    # move (0, 0) to the center
    translate(width()/2, height()/2)

    myCenteredRect(500, 500)
    # set the fill color
    fill(1, 0, 0)
    myCenteredRect(250, 250)
    fill(0, 1, 0)
    myCenteredRect(320, 150)

# when we dedent, we exit the saved state
# and the original canvas settings are preserved
# (black, (0, 0) at lower left)
oval(0, 0, 500, 500)
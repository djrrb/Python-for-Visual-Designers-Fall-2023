def myCenteredRect(myW, myH):
    print('this is a centered rectangle', myW, myH)
    rect(-myW/2, -myH/2, myW, myH)

with savedState():
    

    # move to the middle of the page
    translate(width()/2, height()/2)

    myCenteredRect(500, 500)
    fill(1, 0, 0)
    myCenteredRect(250, 250)
    fill(0, 1, 0)
    myCenteredRect(320, 150)

oval(0, 0, 500, 500)
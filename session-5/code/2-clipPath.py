# define a formatted string
myString = FormattedString('Hi!', fontSize=750)
# we could draw the text to canvas, but let's not
#text(myString, (0, 0))

# instead let's create a bezier path
# and feed our text into the path
myShape = BezierPath()
myShape.text(myString) # like "create outlines" in illustrator

# we could draw this path to canvas, but let's not
#drawPath(myShape)

# let's make a saved state
# all canvas formatting inside will be undone
# when we dedent out of the state
with savedState():
    # set the clip path to our bezier shape
    # anything outside of the shape won't be visible
    clipPath(myShape)
    # now let's draw a bunch of circles
    for myNumber in range(1000):
        fill(random(), random(), random())
        oval(randint(0,1000), randint(0,1000), 100, 100)

# now that we have exited the saved state
# our clipping path no longer applies
# and we can draw some text on top of our shape
fill(0)
fontSize(50)
text('hello world', (50, 50))
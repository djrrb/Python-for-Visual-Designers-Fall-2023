# define a custom function
def myFunTextEffect(myTextArgument):
    # everything at this indent will be run
    # when myFunTextEffect() is called
    # it doesn’t matter what we do in here, it’s just a demo
    
    # loop through 10 numbers
    for myNumber in range(5):
        # get a random x and y a certain offset from our (0, 0)
        myX = randint(-10, 10)
        myY = randint(-10, 10)
        # set a random fill color
        fill(random(), random(), random())
        # set a font size
        fontSize(160)
        # set the text, using the argument provided in the function
        text(myTextArgument, (myX, myY))
    # on top, draw the text one last time in white
    fill(1)
    text(myTextArgument, (0, 0))

# when we dedent, we have left our function
# move away from the margin
translate(100, 100)
# draw some text using our funky text effect
# we provide the text to draw as an argument
# this will run the code in the indented block above
myFunTextEffect('some text')
# move up some more
translate(0, 200)
# now do more text with our fun effect
# running the indented code above a second time
myFunTextEffect('more text')
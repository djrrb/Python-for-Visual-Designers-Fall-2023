# set the font and font size
font('MinionPro-Regular')
fontSize(100)

# loop through 'hello world'

# it will go through each character in that string and assign it to the letter variable

# if we want more letters we can multiply hello world by a certain amount, like 10

for letter in 'hello world'*10:
    
    # make a variable for x

    # if random() is a number between 0 and 1, and width() is thef full width of the canvas, random()*width() will give us a random x coordinate between 0 and the full width.
    x = random()*width()

    # same thing for height!
    y = random()*height()

    # let’s print the current letter we are 
    print(letter, x, y)

    # make it a random color because why not
    fill(random(), random(), random())
    
    # draw the text
    # instead of drawing the entire "hello world" string, just draw the individual letter
    text(letter, (x, y))
    
saveImage('randomPlacementLoop.png')
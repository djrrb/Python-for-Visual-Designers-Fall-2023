# make a notebook-sized page
inch = 72
newPage(7.48*inch, 9.84*inch)

# set a radius for our dots
radius = 10

# make a LOT of circles
for myNumber in range(3000):
    # random()*width() is a random point between 0 and the full width of the canvas (width()).
    x = random()*width()-radius
    y = random()*height()-radius
    oval(x, y, radius*2, radius*2)
  
# draw a white background in the middle
fill(1)
rect(100, 295, width()-200, 200)

# set the fill to black and the font to courier, because...composition!
fill(0)
font('Courier New Bold')
# i’m just gonna fudge the font size so it fits
# we _could_ calculate this, but I’ll save that for later ;-)  
fontSize(20)
# draw the text with a 100pt border
text('Composition Notebook', (148, 390))

saveImage('composition-notebook.png')
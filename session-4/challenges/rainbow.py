# compile a list of colors
myColorList = [
    (1, 0, 0), # red
    (1, .65, 0), # orange
    (1, 1, 0), # yellow
    (0, 1, 0), # green
    (93/255, 208/255, 1), # blue
    (50/255, 60/255, 190/255), # indigo
    (238/255, 130/255, 238/255), # violet,
    (1, 1, 1) # white
    ]

newPage(2000, 1000)
# white background
fill(1)
rect(0, 0, width(), height())

# move to bottom center
translate(width()/2)

# set a starting radius
myRadius = height()
myStripeWidth = 100
for myColor in myColorList:
    fill(*myColor)
    oval(-myRadius, -myRadius, myRadius*2, myRadius*2)
    # each time, make the radius a bit smaller
    myRadius -= myStripeWidth
    
saveImage('rainbow.png')
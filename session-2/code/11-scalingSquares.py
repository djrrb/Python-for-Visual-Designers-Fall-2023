# a variable to store the amount that we will scale
# the canvas after each rectangle
myScaleValue = .9

# how wide is our initial stroke
myStrokeWidth = 5

# determine our shape size
# the stroke will be added equally to the inside and outside of the shape
# so if we want to show the full stroke, we will make it slightly smaller than the canvas
myShapeSize = width()-myStrokeWidth

# move to the center of the canvas
translate(width()/2, height()/2)

# set the stroke color to red
stroke(1, 0, 0)
# set the fill color to None, a special Python keyword
fill(None)

# loop through 50 numbers
# we will draw a shape for each one
for myNumber in range(50):
    # set the stroke width
    strokeWidth(myStrokeWidth)
    print(myStrokeWidth)
    
    # set a centered rectangle
    rect(-myShapeSize/2, -myShapeSize/2, myShapeSize, myShapeSize)
    
    # scale the canvas by our scale value
    scale(myScaleValue)
    
    # counteract the effect of scaling on our stroke width
    # by increasing it by our scale value each time
    # since our scale value is less than 1, dividing by that will
    # increase the number
    myStrokeWidth /= myScaleValue

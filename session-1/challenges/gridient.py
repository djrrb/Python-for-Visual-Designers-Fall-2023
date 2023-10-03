# make a gradient grid by manipulating red, green, blue values

newPage(1000, 1000)

# make some variables for x and y
x = 0
y = 0

# make some variables for red, green, and blue
r = 0
g = 0
b = 0


# instead of looping through a string
# i'm gonna loop through a range of numbers
rows = 10
cols = 10
gridSize = 100

# do our grid loop
for row in range(rows):
    for col in range(cols):
        # set the fill color every time
        fill(r, g, b)
        rect(x, y, gridSize, gridSize)
        x = x + gridSize
        # for each column, make it a little more red
        r = r + 0.1
    # exit the inner loop 
    # do our grid stuff, make y bigger for each row
    y = y + gridSize
    # move x back to 0
    x = 0
    # ALSO
    # for each row, make our blues a little bluer
    b = b + 0.1
    # set red back to 0
    r = 0
    
saveImage('gridient.png')

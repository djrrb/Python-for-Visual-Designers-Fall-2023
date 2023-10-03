# make a checkerboard

# instead of drawing one rectangle for each cell in the grid, draw two

newPage(1000, 1000)

x = 0
y = 0

# instead of looping through a string
# i'm gonna loop through a range of numbers
rows = 10
cols = 10

gridSize = width()/rows

# draw the first set in red
# so you can see the pattern that is getting repeated
fill(1, 0, 0)

for row in range(rows):
    for col in range(cols):
        rect(x, y, gridSize, gridSize)
        rect(x+gridSize, y+gridSize, gridSize, gridSize)
        fill(0)
        x = x + gridSize*2
    y = y + gridSize*2
    x = 0

saveImage('checkerboard.png')
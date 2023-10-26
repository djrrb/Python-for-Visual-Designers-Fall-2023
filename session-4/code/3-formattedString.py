# simple text drawing
#font('Comic Sans MS', 100)
#fill(1, 0, 0)
#text('Hello world', (0, 0))

# something more complex, that carries its own formatting
myString = FormattedString(
    'hello', # the string i want to draw
    font='Comic Sans MS', # the font
    fontSize=100, # font size
    fill=(1, 0, 0) # fill color
)

# we can add new formatting blocks
myString.append(
    ' world', 
    font='Minion Pro', 
    fontSize=200, 
    fill=(0, 0, 1)
)

# and another
myString.append('!', fontSize=50, fill=(0, 1, 0))

# draw the text to the canvas
text(myString, (110, 150))
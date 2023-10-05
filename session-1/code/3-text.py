# print "hello world" to the console
print('hello world')

# set the font 
font('Times')
# set the font size
fontSize(50)
# draw "hello world" to the canvas
# the text() function takes two arguments:
# the string to display ("hello world")
# # an (x, y) tuple that represents the lower left of the page
text('hello world', (0, 0))

# set the fill color 
# fill can take 
# - 1 argument (greyscale)
# - 3 arguments (red, green, blue)
# - 4 arguments (red, green, blue, alpha)

# this will not apply retroactively to things 
# that have already been drawn to the canvas
# but it will apply to everything after
fill(45/255)
text('more text', (100, 100))
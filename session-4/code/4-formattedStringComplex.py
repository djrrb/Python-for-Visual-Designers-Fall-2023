# make a margin
myMargin = 50

# open our text file
# define it as the variable myFile
with open('book.txt', encoding='utf-8') as myFile:
    # read the file into our myText variable
    myText = myFile.read()

# format the text variable as a formatted string
myString = FormattedString(myText, font='Comic Sans MS', fontSize=40, lineHeight=70, tracking=0, fill=(1, 0, 0))

# draw the bounds of our text box so we can seet them
rect(
    myMargin, # x
    myMargin, # y
    width()-myMargin*2, # width, account for both margins
    height()-myMargin*2 # height, account for both margins
)
# draw the text box to canvas
textBox(
    myString, 
    (
        myMargin, 
        myMargin, 
        width()-myMargin*2, 
        height()-myMargin*2
    )
)
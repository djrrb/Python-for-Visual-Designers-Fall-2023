# import the csv module
import csv

# set the card variables
myCSVPath = 'Business Cards - Sheet1.csv'
myInch = 72
myMargin = 20
myCenterMargin = 10
debug = False

# define the logo image
myLogoImage = ImageObject('logo.png')

# a function that draws a single card
def drawCard(row, box):
    myX, myY, myWidth, myHeight = box
    with savedState():
        # move to the margin
        translate(myX, myY)
        with savedState():
            lineDash(2)
            fill(None)
            stroke(.9)
            rect(0, 0, myWidth, myHeight)
        translate(myMargin, myMargin)

        # draw the logo
        myLogoWidth = 75
        myLogoScale = myLogoWidth / myLogoImage.size()[0]
        with savedState():
            # save the state so the change in scale is only temporary
            scale(myLogoScale)
            image(myLogoImage, (0, -1))
        # calculate the text box
        myTextBoxWidth = myWidth - myMargin*2 - myLogoWidth
        myTextBoxHeight = myHeight-myMargin*2
        # draw the text box in debug mode
        fill(.9)
        if debug: rect(myLogoWidth, 0, myTextBoxWidth, myTextBoxHeight)

        # make a new formatted string 
        myText = FormattedString(
            myName, 
            font='ComicSansMS',
            fill=(1, 0, 0)
        )
        # append new text with new formatting
        myText.append(
            '\n\n'+myAddress.strip(), 
            font='MinionPro-Regular',
            openTypeFeatures=dict(smcp=True),
            fill=(0, 0, 0)
            )
        # and more text
        myText.append('\n\n'+myPhone)
        # and more text
        myText.append(
            '\n\n'+myEmail.lower(), 
            openTypeFeatures=dict(resetFeatures=True), 
            font="Minion Pro Italic"
        )

        if debug: print(myText)
        
        # now draw the text box
        # it takes the string (or FormattedString) to draw
        # and also a (x,y,w,h) tuple 
        textBox(myText, 
            (
                myLogoWidth+myCenterMargin,  # x
                0, # y
                myTextBoxWidth, # width
                myTextBoxHeight # height
            )
        )
        
#########
#########
#########
# now let’s make a contact sheet
#########
#########
#########

# set the size and make the first page
myContactSheetSize = 'Letter'
newPage(myContactSheetSize)

# determine the dimensions of the card on the contact sheet
myCardWidth = 3.5*myInch
myCardHeight = 2*myInch

# do a little math to figure out how many cards we can fit on a page
# int() rounds down
myCardsPerRow = int(width()/myCardWidth)
myCardsPerCol = int(height()/myCardHeight)

# if we want to center the cards, figure out the margin we’d need to fit all those card on the page
myContactSheetMarginX = (width()-myCardWidth*myCardsPerRow)/2
myContactSheetMarginY = (height()-myCardHeight*myCardsPerCol)/2
myX = myContactSheetMarginX
myY = myContactSheetMarginY


# open the csv as a file
with open(myCSVPath) as myCSVFile:
    # read the file using the csv reader
    myReader = csv.reader(myCSVFile)
    # loop through each row in the csv
    # where myRow is a list of columns
    # and myRowIndex is what number row we are on, starting at 0
    for myRowIndex, myRow in enumerate(myReader):
        # skip the first row
        if myRowIndex == 0:
            continue
        # unpack the columns into variables
        myName, myAddress, myPhone, myEmail = myRow
        # draw the card using the my card function
        drawCard(myRow, (myX, myY, 3.5*myInch, 2*myInch))
        
        # by default let’s move over to the right to draw
        # the next card
        myX += myCardWidth
        # BUT if the card won’t fit on the page...
        if myX+myCardWidth > width():
            # return X to the left side
            myX = myContactSheetMarginX
            # and move Y up to the next row
            myY += myCardHeight
            # AND if we also exceed the page height
            if myY + myCardHeight > height():
                # make a new page
                newPage(myContactSheetSize)
                # and move Y back to the bottom so we start fresh
                myY = myContactSheetMarginY
                
# our last dedent closes the CSV file
    
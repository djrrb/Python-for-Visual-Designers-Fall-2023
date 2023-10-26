# in this script i am just fudging the positions
# i did it by eye
# but of course you could also set them relative to each other as variablesa

# import the csv library
import csv
# define an inch as 72 point
myInch = 72
# open our csv file and assign it to a variable myFile
with open('Fantasy Conference - Sheet 1.csv', encoding='utf-8') as myFile:
    # read myFile as a CSV using our CSV reader
    myCSV = csv.reader(myFile)
    # loop through each row in the CSV
    for myRow in myCSV:
        # unpack each column into its own variable
        myName, myCompany, myRole = myRow
        print(myName)
        # make a new page, business card size
        newPage(3.5*myInch, 2*myInch)
        # set the font and opentype features
        font('Minion Pro', 18)
        openTypeFeatures(smcp=True)
        # draw a text box with the name
        # define the right side of the box relative to the canvas width
        #rect(20, 70, width()-110, 50)
        textBox(myName, (20, 70, width()-110, 50))
        # draw the affiliation in red in the bottom left
        fill(1, 0, 0)
        openTypeFeatures(smcp=False)
        fontSize(12)
        text(myCompany, (20, 30))
        # scale the canvas so that the image draws correctly
        scale(.4)
        # draw the logo
        image('https://universityinnovation.org/images/5/5c/Cooper_union_logo.png', (420, 130))
        
# import the shuffle function from the random library
from random import shuffle
# import hsv_to_rgb from the color sys library
from colorsys import hsv_to_rgb

# get words from the internal mac dictionary
# (sorry if the words are gross or offensive!)
myWordsPath = '/usr/share/dict/words'

# set a default saturation and value
# we will select the hue randomly for each word
sat = .5
val = 1

# make an empty string that we will add to over time
myString = FormattedString(
    font = 'Georgia',
    fontSize = 30,
    align = 'center'
    )

# draw a background
rect(0, 0, width(), height())

# open the mac internal dictionary as a file
# it has a word on each line
with open(myWordsPath, encoding='utf-8') as wordsFile:
    # read each line into a list using file.readlines()
    myWords = wordsFile.readlines()
    # shuffle the lines in the list so they are in a random order
    shuffle(myWords)
    # we don’t want this to take all day, so cap it at 1000 words
    myWords = myWords[:1000]
    
    # loop through the words
    for myWord in myWords:
        # for each word, append it to our formattedstring
        # oops, looks like this file includes some whitespace attached to each word, so we can strip it out
        # also set the fill to a semirandom RGB value
        myRGB = hsv_to_rgb(random(), sat, val)
        myString.append(
            myWord.strip() + ' ',
            fill=myRGB
            )
        
# now draw that formatted string to the canvas
# set some constants
margin = 100
contentWidth = width()-margin*2
contentHeight = height()-margin*2
# draw a text box with the formatted string
textBox(myString, (margin, margin, contentHeight, contentWidth))

saveImage('randomWordGenerator.png')
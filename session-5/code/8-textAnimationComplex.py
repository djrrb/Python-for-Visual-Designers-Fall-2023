# how many circles to draw
myShapeCount = 50
# what size to make them (as wide as we need to fit 50 on the page)
myShapeSize = width()/myShapeCount
# draw as many frames as we have shapes
# so there will be one shape per frame
myFrameCount = myShapeCount

# loop through each frame
for myFrameNumber in range(myFrameCount):
    # make a new page
    newPage()
    # make a white background
    fill(1)
    rect(0, 0, width(), height())
    # draw all remaining shapes in black
    fill(0)
    frameDuration(1/24)
    translate(0, height()/2)
    # set the font and font size
    font('CondorVariable-VF.ttf')
    fontSize(800)
    # get information from the font about its variable axes
    # listFontVariations() gives us a dictionary, which we can query by axis
    # that gives us another dictionary that we can query by attribute (name, minValue, maxValue, defaultValue)
    myMinValue = listFontVariations()['wght']['minValue']
    myMaxValue = listFontVariations()['wght']['maxValue']
    # also get italics
    myItalMinValue = listFontVariations()['ital']['minValue']
    myItalMaxValue = listFontVariations()['ital']['maxValue']

    # loop through each shape
    for myShapeNumber in range(myShapeCount):
        # only draw a shape if we are on the right frame
        if myShapeNumber == myFrameNumber:
        #if True:
            # how far are we through the sequence, between 0 and 1
            myProgress = myShapeNumber / myShapeCount
            # use sin() and 2*pi to find where we are on a circle
            myCurvature = sin(2*pi*myProgress)
            # do the same for italics, but this time go full circle twice (4*pi)
            myItalCurvature = cos(4*pi*myProgress)
            # how tall will our wave be (half the canvas height, so it can go above and below)
            myWaveSize = height()/2
            # what is the y position of our waveform
            myY = myCurvature*myWaveSize
            # use our same curvature information to get the corresponding value
            # on the variable axis by finding how our value is situated between (-1, 1)
            # and remapping it to our axis range
            myWeightValue = remap(myCurvature, -1, 1, myMinValue, myMaxValue)
            # same for italic axis
            myItalicValue = remap(myItalCurvature, -1, 1, myItalMinValue, myItalMaxValue)
            print(myWeightValue)
            # set the font variations for weight and italic
            fontVariations(wght=myWeightValue, ital=myItalicValue)
            # draw our text to canvas
            text('Hello', (width()/2, -230), align="center")
            
            # draw an oval to show the waveform
            # the x position is sequential from left to right
            myX = myShapeNumber*myShapeSize
            fill(1, 0, 0)
            oval(myX, myY, myShapeSize, myShapeSize)
        
saveImage('textAnimation.gif')
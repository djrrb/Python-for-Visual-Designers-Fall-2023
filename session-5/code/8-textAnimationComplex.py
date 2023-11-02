myShapeCount = 50
myShapeSize = 20
myFrameCount = myShapeCount

for myFrameNumber in range(myFrameCount):
    newPage()
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    frameDuration(1/24)
    translate(0, height()/2)
    
    font('CondorVariable-VF.ttf')
    fontSize(800)
    myMinValue = listFontVariations()['wght']['minValue']
    myMaxValue = listFontVariations()['wght']['maxValue']
    myItalMinValue = listFontVariations()['ital']['minValue']
    myItalMaxValue = listFontVariations()['ital']['maxValue']
    myValueRange = myMaxValue - myMinValue

    for myShapeNumber in range(myShapeCount):
        if myShapeNumber == myFrameNumber:
        #if True:
            myProgress = myShapeNumber / myShapeCount
            myCurvature = sin(2*pi*myProgress)
            myItalCurvature = cos(4*pi*myProgress)
            myWaveSize = height()/2
            myY = myCurvature*myWaveSize
            myWeightValue = remap(myCurvature, -1, 1, myMinValue, myMaxValue)
            myItalicValue = remap(myItalCurvature, -1, 1, myItalMinValue, myItalMaxValue)
            print(myWeightValue)
            fontVariations(wght=myWeightValue, ital=myItalicValue)
            text('Hello', (width()/2, -230), align="center")
            myX = myShapeNumber*myShapeSize
            #myX = width()/2
            oval(myX, myY, myShapeSize, myShapeSize)
        
saveImage('moveAcrossPage.gif')
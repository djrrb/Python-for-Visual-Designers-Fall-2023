myMargin = -500
myLineCount = 500
lineCap('round')

rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)

for myLineNumber in range(myLineCount):
    stroke(random(), random(), random())
    strokeWidth(10)
    myStartX = randint(myMargin, width()-myMargin)
    myStartY = randint(myMargin, height()-myMargin)
    myEndX = randint(myMargin, width()-myMargin)
    myEndY = randint(myMargin, height()-myMargin)
    line((myStartX, myStartY), (myEndX, myEndY))


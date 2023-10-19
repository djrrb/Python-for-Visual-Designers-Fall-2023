# let’s make a grid!

newPage('A4Landscape')

myXCount, myYCount = 10, 10
myShapeWidth, myShapeHeight = width()/myXCount, height()/myYCount

print(list(range(myXCount)))


# this will run once
for myYNumber in range(myYCount):
    
    # this will run 10 times
    print('begin row number', myYNumber)
    for myXNumber in range(myXCount):
        fill(random(), random(), random())
        # this will run 100 times
        myX = myXNumber * myShapeWidth
        myY = myYNumber * myShapeHeight
        print('\tcol', myXNumber, myX)
        # oval(x, y, width, height)
        oval(myX, myY, myShapeWidth, myShapeHeight)
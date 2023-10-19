mySegmentCount = 100
myPointList = []
for mySegmentNumber in range(mySegmentCount):
    myX = randint(0, width())
    myY = randint(0, height())
    myPointList.append((myX, myY))
    print(myPointList)

stroke(1, 0, 0)
#line( (0, 0), (50, 50) )

polygon(*myPointList)
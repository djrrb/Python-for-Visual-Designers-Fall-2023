# let’s make a grid!

myXCount, myYCount = 10, 10
myShapeWidth, myShapeHeight = 100, 100

print(list(range(myXCount)))

for myXNumber in range(myXCount):
    myX = myXNumber * myShapeWidth
    print('col', myXNumber, myX)
    # oval(x, y, width, height)
    oval(myX, 0, myShapeWidth, myShapeHeight)
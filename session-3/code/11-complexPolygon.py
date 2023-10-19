# how many segments will we draw
mySegmentCount = 100
# make an empty list
# we will add points to it
myPointList = []

# loop through our number range
for mySegmentNumber in range(mySegmentCount):
    # get a random (x, y) coordinate
    myX = randint(0, width())
    myY = randint(0, height())
    # append our random (x, y) tuple to the end of the list
    myPointList.append((myX, myY))
    # print to watch the list grow
    print(myPointList)

# make the stroke red
stroke(1, 0, 0)
# no fill
fill(None)
# draw a polygon
# use * to unpack the list of points 
# to feed each (x, y) to polygon() separately
polygon(*myPointList)
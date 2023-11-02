myString = FormattedString('H', fontSize=800)

blendMode('overlay')

#text(myString, (0, 0))

myShape = BezierPath()
myShape.text(myString) # like "create outlines"

#drawPath(myShape)

with savedState():
    clipPath(myShape)
    for myNumber in range(1000):
        fill(random(), random(), random())
        oval(randint(0,1000), randint(0,1000), 100, 100)
    
fill(0)
fontSize(50)
text('hello world', (50, 50))
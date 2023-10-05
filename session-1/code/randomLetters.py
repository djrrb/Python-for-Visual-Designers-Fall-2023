myString = 'the quick brown fox'

for myPage in range(0, 10):
    print(myPage)
    newPage()
    for myLetter in myString:
        myX = randint(0, width())
        myY = randint(0, height())
        fontSize(100)
        fill(random(), random(), random())
        text(myLetter, (myX, myY))
        
saveImage('myImage.gif')
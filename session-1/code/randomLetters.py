myString = 'the quick brown fox'


for myPage in range(0, 10):
    print(myPage)
    newPage()
    frameDuration(1/30)
    rect(0, 0, width(), height())
    
    for myLetter in myString:
        myX = randint(0, width())
        myY = randint(0, height())
        fontSize(130)
        fill(random(), random(), random())
        text(myLetter, (myX, myY))
        
        
    #saveImage('myImage'+str(myPage)+'.png')
    
saveImage('myImage.gif')
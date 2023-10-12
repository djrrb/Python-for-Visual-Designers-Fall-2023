for myNumber in range(10):
    print(myNumber)
    newPage()
    fill(random(), random(), random())
    rect(0, 0, width(), height())
    saveImage('randomColors.gif')
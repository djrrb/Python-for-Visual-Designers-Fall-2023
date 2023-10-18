# how many numbers to draw
myFrameCount = 100

# loop trhough each number
for myFrameNumber in range(myFrameCount):
    # make an new page
    newPage()
    # set the font size
    fontSize(700)
    
    # % is the modulo operator
    # it will return the remainder after a whole number division
    # 5 / 2 = 2.5
    # 5 // 2 = 2 (how many times does 2 go into 5? 2 times)
    # 5 % 2 = 1 (what remainder is left over? 1)
    # for even numbers, there will be no remainder
    # for odd numbers, there will be a remainder
    
    # if there is a remainder after dividing by 2
    if myFrameNumber % 2:
        # set the color to red for odd numbers
        fill(1, 0, 0)
        # also print to console
        print(myFrameNumber, 'is odd')
    # otherwise, the number is even
    else:
        # set the color to blue
        fill(0, 0, 1)
        # and print to console
        print(myFrameNumber, 'is even')
        
    # str(myFrameNumber) converts the integer to a string
    text(str(myFrameNumber), ( width()/2, 250 ), align="center")
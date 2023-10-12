# stuff at this indent is run 1 time

# create a list
myGroceryList = ['apples', 'oranges', 'bananas']

# set a starting point for x and y
myX = 500
myY = 100
# get one random alpha value and store it in a variable
myRandomAlpha = random()
print('random alpha:', myRandomAlpha)

for myGroceryItem in myGroceryList:
    # myGroceryItem = apples, then oranges, then bananas
    print(myGroceryItem)
    # code at this indent is run 3 times

    # now loop through each character in the grocery item    
    for myChar in myGroceryItem:
        # code at this indent is run once for every letter
        # within every list item (total: 19 times)
        print(myChar)

        fontSize(100)
        # set the fill to a random color each time
        # but use the alpha we calculated at the beginning
        fill(random(), random(),random(), myRandomAlpha)

        # draw the text to canvas at our coordinates
        text(myChar, (myX, myY))

        # augment the y variable for each letter
        myY += 40
        print(myY)
    # dedent, now we are back to running once per list item
    # augment the X variable once per list item
    myX += 40
    
# back to running one time
print('we are done with the loop')    

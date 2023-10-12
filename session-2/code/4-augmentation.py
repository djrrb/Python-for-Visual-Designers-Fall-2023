# stuff at this indent is run 1 time

# create a list
myGroceryList = ['apples', 'oranges', 'bananas']

# set a starting point for x and y
myX = 500
myY = 100
# get one random alpha value and store it in a variable
myRandomAlpha = random()
print('random alpha:', myRandomAlpha)

# loop through the grocery list
for myGroceryItem in myGroceryList:
    # myGroceryItem = apples, then oranges, then bananas
    print(myGroceryItem)
    # code at this indent is run 3 times
    
    # set the font size
    fontSize(100)
    # set the fill to a random color each time
    # but use the alpha we calculated at the beginning
    fill(random(), random(),random(), myRandomAlpha)

    # draw the text to canvas at our coordinates
    text(myGroceryItem, (myX, myY))
    # augment the myY variable so it gets bigger every time
    #myY = myY - 100 # longhand
    myY += 100 # shorthand
    print('myY:', myY) 
    
# dedent to exit the loop
# all code at this indent runs one time
print('we are done with the loop')    

# the last grocery item is still bananas
print(myGroceryItem)
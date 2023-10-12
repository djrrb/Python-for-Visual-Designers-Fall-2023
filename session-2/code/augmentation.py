# stuff at this indent is run 1 time

# create a list
myGroceryList = ['apples', 'oranges', 'bananas']
myX = 500
myY = 100
myRandomAlpha = random()
print(myRandomAlpha)

for myGroceryItem in myGroceryList:
    # stuff at this indent is run 3 times
    print(myGroceryItem)
    fontSize(100)
    fill(random(), random(),random(), myRandomAlpha)

    text(myGroceryItem, (myX, myY))
    #myY = myY - 100    
    myY += 100
    print(myY)
    
# back to running one time
print('we are done with the loop')    

print(myGroceryItem)
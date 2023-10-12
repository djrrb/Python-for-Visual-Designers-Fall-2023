# create a list of strings
myGroceryList = ['apples', 'oranges', 'bananas']

# give us the length
print('length:', len(myGroceryList))

# slice the list to give us a particular item
# list indices begin with 0
# so myGroceryList[2] will give us the third item in the list
print('third item:', myGroceryList[2])

# slice a portion of the list
# [:2] will give us the first two items from the list
print('first two items:', myGroceryList[:2])
# [-2:] will give us the last two items from the list
print('last two items:', myGroceryList[-2:])

# give me a copy of a sorted list (alphabetically)
mySortedList = sorted(myGroceryList)
print('a sorted copy:', mySortedList)

# sort a list in place
#myGroceryList.sort(reverse=True)

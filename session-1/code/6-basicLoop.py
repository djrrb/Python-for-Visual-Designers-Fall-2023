# let's loop through a sequence
# doing something to each item in the sequence one at a time

# create a variable called myString
myString = 'hello world'

# loop through each letter in the string
# myLetter is a variable we create that will be equal to the current item in the sequence
for myLetter in myString:   
    # print each letter, one at a time
    # all code that is indented will run once for each item in the sequence
    print(myLetter)

# once we dedent, we exit the loop, and the following code will only be run once
print('done')
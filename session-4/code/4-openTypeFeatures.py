#font('Comic Sans MS', 100)
#fill(1, 0, 0)
#text('Hello world', (0, 0))

myMargin = 50

with open('book.txt', encoding='utf-8') as myFile:
    myText = myFile.read()

myString = FormattedString(myText, font='Comic Sans MS', fontSize=40, lineHeight=70, tracking=0, fill=(1, 0, 0))

myString.append(' world', font='Minion Pro', fontSize=200, fill=(0, 0, 1))

myString.append('!', fontSize=50, fill=(0, 1, 0))

rect(myMargin, myMargin, width()-myMargin*2, height()-myMargin*2)
textBox(myString, (myMargin, myMargin, width()-myMargin*2, height()-myMargin*2))
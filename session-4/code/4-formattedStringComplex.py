#font('Comic Sans MS', 100)
#fill(1, 0, 0)
#text('Hello world', (0, 0))

myString = FormattedString('hello', font='Comic Sans MS', fontSize=100, fill=(1, 0, 0))

myString.append(' world', font='Minion Pro', fontSize=200, fill=(0, 0, 1))

myString.append('!', fontSize=50, fill=(0, 1, 0))

text(myString, (110, 150))
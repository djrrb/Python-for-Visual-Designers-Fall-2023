myText = 'WORD'

newPage(1200, 350)


fontSize(200)
font('NickelGothicv2-Wide')

translate(width()/2, 100)
with savedState():
    fill(.7)
    scale(1, .9)
    skew(-10)
    text(myText, (0, 0), align="center")

text(myText, (0, 0), align="center")

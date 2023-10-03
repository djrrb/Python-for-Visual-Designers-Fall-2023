red = (168/255, 13/255, 48/255)
grey = (.4,)
black = (.1,)
white = (.9,)

w1 = 130
sw = w1/20

def pattern():
    fill(*black)
    rect(0, 0, w1, w1)
    fill(*red)
    rect(w1, 0, w1, w1)
    fill(*red)
    rect(0, w1, w1, w1)
    fill(*grey)
    rect(w1, w1, w1, w1)
    stroke(*grey)
    strokeWidth(sw)
    line((w1/2, 0), (w1/2, w1*2))
    line((0, w1/2), (w1*2, w1/2))
    stroke(*black)
    line((w1+w1/2, 0), (w1+w1/2, w1*2))
    line((0, w1+w1/2), (w1*2, w1+w1/2))
    stroke(None)

newPage(1000, 1000)

scale(1, 1.3)
translate(width()/4, -height()*.9)
rotate(45)
for y in range(20):
    with savedState():
        for x in range(10):
            pattern()
            translate(w1*2)
    translate(0, w1*2)

saveImage('pattern-example-argyle.png')
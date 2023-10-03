red = 1, .2, .2, 1
darkGreen = 0, 0, 0, .5
lightGreen = 178/255, 206/255, 93/255, .5
bg = 12/255, 114/255, 85/255



newPage(1000, 1000)


fill(*bg)
rect(0, 0, width(), height())

# width and height of a single block of the pattern
w = 500
h = 500

# base stripe thickness
b = 6.85/1000*w

blendMode('overlay')

# start off canvas
translate(-b*3.5, -b*3.5)

# make a grid 
for y in range(0, height()+h, h):
    for x in range(0, width()+w, w):
        # no shortcuts here just draw the pattern
        # including b in each value makes it easier to scale
        fill(*red)
        rect(x, y, w, b)
        rect(x, y+b*3, w, b)
        rect(x, y+b*6, w, b)
        rect(x, y+b*69, w, b)
        rect(x, y+b*72, w, b)
        rect(x, y+b*75, w, b)
        rect(x, y, b, h)
        rect(x+b*3, y, b, h)
        rect(x+b*6, y, b, h)
        rect(x+b*69, y, b, h)
        rect(x+b*72, y, b, h)
        rect(x+b*75, y, b, h)
        

        fill(*darkGreen)
        rect(x, y+b*21, w, b*3)
        rect(x, y+b*26, w, b*3)
        rect(x, y+b*47, w, b*3)
        rect(x, y+b*52, w, b*3)

        rect(x, y+b*90, w, b*3)
        rect(x, y+b*95, w, b*3)
        rect(x, y+b*124, w, b*3)
        rect(x, y+b*129, w, b*3)

        rect(x+b*21, y, b*3, h)
        rect(x+b*26, y, b*3, h)
        rect(x+b*47, y, b*3, h)
        rect(x+b*52, y, b*3, h)
    
        rect(x+b*90, y, b*3, h)
        rect(x+b*95, y, b*3, h)
        rect(x+b*124, y, b*3, h)
        rect(x+b*129, y, b*3, h)

        fill(*lightGreen)
        rect(x, y+b*32, w, b)
        rect(x, y+b*35, w, b)
        rect(x, y+b*40, w, b)
        rect(x, y+b*43, w, b)
    
        rect(x, y+b*101, w, b)
        rect(x, y+b*104, w, b)
        rect(x, y+b*107, w, b*3)
        rect(x, y+b*112, w, b*3)
        rect(x, y+b*117, w, b)
        rect(x, y+b*120, w, b)
    
    
        rect(x+b*32, y, b, h)
        rect(x+b*35, y, b, h)
        rect(x+b*40, y, b, h)
        rect(x+b*43, y, b, h)
    
        rect(x+b*101, y, b, h)
        rect(x+b*104, y, b, h)
        rect(x+b*107, y, b*3, h)
        rect(x+b*112, y, b*3, h)
        rect(x+b*117, y, b, h)
        rect(x+b*120, y, b, h) 

saveImage('pattern-example-plaid.png')
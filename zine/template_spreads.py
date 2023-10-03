# spreads are a little more complicated!

# define our constants
inch = 72
cropWidth = 5.83 * inch 
cropHeight = 8.27 * inch
bleed = 0.125 * inch

# do i want to see the bleed?
# make this false before exporting
drawBleed = False

# calculate the total width and height
totalWidth = cropWidth*2+bleed*2
totalHeight = cropHeight+bleed*2

# make a new page
newPage(totalWidth, totalHeight)


with savedState():
    if drawBleed:    
        # draw the crop areas
        stroke(1, 0, 0)
        fill(None)
        strokeWidth(.5)
        rect(bleed, bleed, cropWidth, cropHeight)
        rect(cropWidth+bleed, bleed, cropWidth, cropHeight)
        # draw individual pages
        stroke(0, .5, 1)
        rect(0, 0, cropWidth+bleed*2, cropHeight+bleed*2)
        rect(cropWidth, 0, cropWidth+bleed*2, cropHeight+bleed*2)
        
# move to the (0, 0) of the cropped page, if you want
translate(bleed, bleed)
fontSize(20)
text('lower left', (0, 0))
with savedState():
    translate(500, 500)
    fill(1, 0, 0)
    text('red and in the middle', (0, 0))
# dedenting exits the saved state
# and undoes all of the canvas transformations we have done
text('b ack to the lower left again', (0, 30))
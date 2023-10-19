fill(1, 0, 0)
oval(0, 0, 100, 100)

with savedState():
    fill(0, 1, 0)
    rotate(20)
    skew(50)
    rect(200, 200, 100, 100)

fontSize(100)
text('hello world', (500, 500))
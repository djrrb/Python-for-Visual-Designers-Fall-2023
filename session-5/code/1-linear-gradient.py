# set a gradient as the fill color
linearGradient(
    (0, 270),                         # startPoint
    (1000, 830),                         # endPoint
    [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
    [0, .5, 1]                          # locations
    )
# draw a rectangle
shadow((-50, -50), 80, (1, 0, 0))

rect(100, 100, 500, 500)
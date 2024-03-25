# set a gradient as the fill color
linearGradient(
    (0, 270),                         # startPoint
    (1000, 830),                         # endPoint
    [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
    [0, .5, 1]                          # locations
    )
# set the shadow value
shadow(
    (-50, -50), # offset
    50, # blur amount, 
    (1, 1, 0) # color, if not black
    )

# draw a shape
rect(100, 100, 500, 500)
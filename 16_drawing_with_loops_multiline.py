# 19 drawing with loops - multiline quotes

import turtle

# draw a box
draw = turtle.Pen()

'''
for x in range(1, 5):
    draw.forward(50)
    draw.left(90)
'''
# draw a mystery object
for x in range(1, 9):
    draw.forward(100)
    draw.left(225)

# freestyle
for x in range(1, 9):
    draw.forward(200)
    draw.right(50)
    draw.right(100)
    draw.left(200)
    draw.right(50)
    draw.right(200)
    draw.left(100)
    draw.right(50)

print("a star is born")

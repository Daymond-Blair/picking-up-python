# 19 drawing with python - loops and conditionals

'''
Types of Operators:

Arithmetic
Comparison
Assignment
Logical

Bitwise
Membership
Identity
'''
import turtle
draw = turtle.Pen()

draw.color('blue', 'green')
draw.begin_fill()

# initialize variables
count = 0

# draw a star
'''
for x in range(1, 14):
    draw.forward(300)
    draw.left(225)
    count = count + 1

    print("Count is: " + str(count))

    # stop drawing after 8 loops
    if count > 7 and count < 12:

    #if count > 7:
        print("The star pattern is complete!")
        break
'''
# draw a square

for i in range(1, 5):
    draw.forward(200)
    draw.right(90)
    draw.forward(200)
    draw.right(90)

    print("squaretime!")
draw.end_fill()
print("A star is born!")

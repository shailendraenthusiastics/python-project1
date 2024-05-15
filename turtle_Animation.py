import turtle as t
t.title("moving the turtle")
t.getscreen()
t.pencolor("yellow")
t.shape("turtle")
t.shapesize(10,10,10)
for angle in range(0,901,90):
    t.left(angle)

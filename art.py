import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")

t.speed(0)
t.width(2)

# Helper function
def draw_circle(color, x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Head
draw_circle("#f4d77f", 0, 50, 80)

# Ears
t.penup()
t.goto(-60, 120)
t.pendown()
t.color("black", "#f4d77f")
t.begin_fill()
t.setheading(120)
t.circle(100, 40)
t.setheading(260)
t.circle(100, 40)
t.end_fill()

t.penup()
t.goto(60, 120)
t.pendown()
t.begin_fill()
t.setheading(60)
t.circle(-100, 40)
t.setheading(-80)
t.circle(-100, 40)
t.end_fill()

# Leaf ears (green parts)
draw_circle("#4CAF50", -95, 155, 30)
draw_circle("#4CAF50", 95, 155, 30)

# Eyes
draw_circle("white", -30, 80, 18)
draw_circle("white", 30, 80, 18)

draw_circle("#8B4513", -30, 80, 10)
draw_circle("#8B4513", 30, 80, 10)

draw_circle("black", -30, 85, 5)
draw_circle("black", 30, 85, 5)

# Nose
draw_circle("black", 0, 60, 5)

# Mouth
t.penup()
t.goto(-15, 50)
t.pendown()
t.setheading(-60)
t.circle(20, 120)

# Leaf on head
t.penup()
t.goto(0, 140)
t.pendown()
t.color("black", "#4CAF50")
t.begin_fill()
t.setheading(90)
t.circle(60, 60)
t.setheading(210)
t.circle(60, 60)
t.end_fill()

t.hideturtle()
turtle.done()

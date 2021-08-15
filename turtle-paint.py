import turtle

wn = turtle.Screen()
wn.title("Turtle Draw Program")
wn.setup(width=800, height=600)

pen = turtle.Turtle()
pen.shapesize(10)

def f():
    pen.color("red")
    y = pen.ycor()
    pen.sety(y + 100)

def b():
    pen.color("blue")
    y = pen.ycor()
    pen.sety(y - 100)

def l():
    pen.color("green")
    x = pen.xcor()
    pen.setx(x-100)

def r():
    pen.color("yellow")
    x = pen.xcor()
    pen.setx(x+100)

wn.listen()
wn.onkeypress(f, "Up")
wn.onkeypress(b, "Down")
wn.onkeypress(l, "Left")
wn.onkeypress(r, "Right")

while True:
    wn.update()
    
    

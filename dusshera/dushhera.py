import turtle
from sketchpy import canvas
import turtle 
obj = canvas.sketch_from_svg("Happy Dussehra.svg")
t = turtle.Turtle()
t.penup()
t.goto(-60,-290)
t.pendown()
t.pencolor("#ff6600")
t.write("Happy Dussehra", align="center", font=("Arial",50,"bold"))
obj.draw()
t.hideturtle()
turtle.done()

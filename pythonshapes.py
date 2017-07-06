from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:

pendown()
color = input('Pick a color:   ')
pencolor (color)
num= input('How many sides?')

for sides in range (int(num)):
    forward (50)
    right (360/(int(num)))


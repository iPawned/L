import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    rad = simpledialog.askinteger(title='Circle Area Calculator',prompt='Enter the radius below:')
    # Make a new turtle
    t = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    t.circle(radius=rad)
    # Call the turtle .penup() method
    t.penup()
    # Move your turtle to a new x,y position using .goto()
    t.goto(0,0)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = (math.pi * rad * rad)
    # Write the area of your circle using the turtle .write() method
    t.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    t.hideturtle()
    # Hide your turtle
    turtle.done()
    # Call turtle.done()

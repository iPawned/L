import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    q = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='',prompt='Do you want to draw a square, triangle, or circle?')
    if shape == 'square':
        for i in range(4):
            q.forward(100)
            q.right(90)
    elif shape == 'triangle':
        for i in range(3):
            q.forward(100)
            q.right(120)
    else:
        q.circle(75)

    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method

import math
import turtle
from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    r = turtle.Turtle()
    areaorcir = simpledialog.askstring(title='Circle Calculator',prompt='Would you like to calculate for area or circumference?')
    if areaorcir == 'area':
        rad1 = simpledialog.askinteger(title='Circle Calculator', prompt='What is the radius of your circle?')
        area = (math.pi * rad1 * rad1)
        r.circle(radius=rad1)
        r.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    elif areaorcir == 'circumference':
        rad2 = simpledialog.askstring(title='Circle Calculator', prompt='What is the radius of your circle?')
        cir = (math.pi * rad2 * 2)
        r.circle(radius=rad2)
        r.write(arg="area = " + str(cir), move=True, align='left', font=('Arial',8,'normal'))

    else:
        messagebox.showinfo(title='Error', message='Please choose either "area" or "circumference"')

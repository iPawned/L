from tkinter import simpledialog, Tk, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(title='Number Adder', prompt='Type the first number you want to add')
    num2 = simpledialog.askinteger(title='Number Adder', prompt='Type the second number you want to add')
    messagebox.showinfo(title='Number Adder', message=num1+num2)

from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(title='Calculator', prompt='Enter the first number you want to calculate:')
    num2 = simpledialog.askinteger(title='Calculator', prompt='Enter the second number you want to calculate:')
    op = simpledialog.askstring(title='Calculator', prompt='Enter the operation you want to do (/ * + -):')
    if op != '/' or op != '*' or op != '+' or op != '-':
        messagebox.showerror(title='', message='Please put a valid operation (/ * + -)')
    if op == '/':
       messagebox.showinfo(title='', prompt= num1 / num2)
    if op == '*':
       messagebox.showinfo(title='', prompt= num1 * num2)
    if op == '+':
       messagebox.showinfo(title='', prompt= num1 + num2)
    if op == '-':
       messagebox.showinfo(title='', prompt= num1 - num2)


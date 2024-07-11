from tkinter import simpledialog, Tk, messagebox

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    age = simpledialog.askinteger(title='', prompt=' How old are you?')
    count = 0
    for i in range(age):
        count += 1
        messagebox.showinfo(title='', message= count)

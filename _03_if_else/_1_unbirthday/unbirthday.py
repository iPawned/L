from tkinter import simpledialog, messagebox

if __name__ == '__main__':
    birthday = simpledialog.askstring(title='', prompt='When is your birthday?')
    if birthday == '7/10':
        messagebox.showinfo('Happy Birthday!')
    else:
        messagebox.showinfo("Have a Merry Unbirthday!")

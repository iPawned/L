from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    point = 0
    riddle1 = simpledialog.askstring(title='Riddle 1', prompt='I am white when I am dirty, and black when I am clean. What am I?')
    if riddle1 == 'a blackboard':
        messagebox.showinfo(title='',message='Correct!')
        point += 1
        print(point)
    else:
        messagebox.showinfo(title='',message='Incorrect')
    riddle2 = simpledialog.askstring(title='Riddle 2', prompt='Davids father has three sons: Snap, Crackle, and _____?')
    if riddle2 == 'David':
        messagebox.showinfo(title='', message='Correct!')
        point += 1
        print(point)
    else:
        messagebox.showinfo(title='', message='Incorrect')
    riddle3 = simpledialog.askstring(title='Riddle 3', prompt='If eleven plus two equals one, what does nine plus five equal?')
    if riddle3 == '2':
        messagebox.showinfo(title='',message='Correct!')
        point += 1
        print(point)
    else:
        messagebox.showinfo(title='',message='Incorrect')
    if point == 3:
        messagebox.showinfo(title='3/3', message='You got all of them right!')
    if point == 2:
        messagebox.showinfo(title='2/3', message='You got only 1 wrong!')
    if point == 1:
        messagebox.showinfo(title='1/3', message='You got 1 right')
    if point == 0:
        messagebox.showinfo(title='0/3', message='You got all of them wrong :(')

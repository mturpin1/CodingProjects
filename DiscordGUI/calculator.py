from tkinter import *
import random

gui = Tk()
gui.title('Calculator GUI')
gui.configure(bg='white')
gui.wm_attributes('-topmost', 1)

entryBox = Entry(gui, width=35, bg='black', fg='white', insertbackground='white', insertwidth=2, insertontime=900, borderwidth=5)
entryBox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonClick(number):
    current = entryBox.get()
    entryBox.delete(0, END)
    entryBox.insert(0, str(current) + str(number))

def buttonClear():
    entryBox.delete(0, END)

def buttonEqual():
    second_number = entryBox.get()
    entryBox.delete(0, END)
    if math == 'addition':
        entryBox.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        entryBox.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        entryBox.insert(0, f_num * int(second_number))
    if math == 'division':
        entryBox.insert(0, f_num / int(second_number))

def buttonAdd():
    first_number = entryBox.get()
    global f_num
    global math
    math = 'addition'
    if isinstance(first_number, int) == True:
        f_num = int(first_number)
    elif isinstance(first_number, float) == True:
        f_num = float(first_number)
    entryBox.delete(0, END)

def buttonSubtract():
    first_number = entryBox.get()
    global f_num
    global math
    math = 'subtraction'
    if isinstance(first_number, int) == True:
        f_num = int(first_number)
    elif isinstance(first_number, float) == True:
        f_num = float(first_number)
    entryBox.delete(0, END)

def buttonMultiply():
    first_number = entryBox.get()
    global f_num
    global math
    math = 'multiplication'
    if isinstance(first_number, int) == True:
        f_num = int(first_number)
    elif isinstance(first_number, float) == True:
        f_num = float(first_number)
    entryBox.delete(0, END)

def buttonDivide():
    first_number = entryBox.get()
    global f_num
    global math
    math = 'division'
    if isinstance(first_number, int) == True:
        f_num = int(first_number)
    elif isinstance(first_number, float) == True:
        f_num = float(first_number)
    entryBox.delete(0, END)

button_1 = Button(gui, text='1', padx=40, pady=20, command=lambda: buttonClick(1)).grid(row=3, column=0)
button_2 = Button(gui, text='2', padx=40, pady=20, command=lambda: buttonClick(2)).grid(row=3, column=1)
button_3 = Button(gui, text='3', padx=40, pady=20, command=lambda: buttonClick(3)).grid(row=3, column=2)
button_4 = Button(gui, text='4', padx=40, pady=20, command=lambda: buttonClick(4)).grid(row=2, column=0)
button_5 = Button(gui, text='5', padx=40, pady=20, command=lambda: buttonClick(5)).grid(row=2, column=1)
button_6 = Button(gui, text='6', padx=40, pady=20, command=lambda: buttonClick(6)).grid(row=2, column=2)
button_7 = Button(gui, text='7', padx=40, pady=20, command=lambda: buttonClick(7)).grid(row=1, column=0)
button_8 = Button(gui, text='8', padx=40, pady=20, command=lambda: buttonClick(8)).grid(row=1, column=1)
button_9 = Button(gui, text='9', padx=40, pady=20, command=lambda: buttonClick(9)).grid(row=1, column=2)
button_0 = Button(gui, text='0', padx=40, pady=20, command=lambda: buttonClick(0)).grid(row=4, column=0)

button_add = Button(gui, text='+', padx=39, pady=20, command=buttonAdd).grid(row=5, column=0)
button_subtract = Button(gui, text='-', padx=40.45, pady=20, command=buttonSubtract).grid(row=6, column=0)
button_multiply = Button(gui, text='x', padx=39, pady=20, command=buttonMultiply).grid(row=5, column=1)
button_divide = Button(gui, text='/', padx=39, pady=20, command=buttonDivide).grid(row=6, column=1)


button_equal = Button(gui, text='=', padx=40, pady=51, command=buttonEqual).grid(row=5, column=2, rowspan=2)

button_clear = Button(gui, text='Clear', padx=76.5, pady=20, command=buttonClear).grid(row=4, column=1, columnspan=2)

gui.mainloop()
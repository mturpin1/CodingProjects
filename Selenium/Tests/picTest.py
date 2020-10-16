import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import NW
from PIL import Image, ImageTk
import picTestVars

root = tk.Tk()
root.geometry(picTestVars.defaultGeometry)

def info(arg1, arg2):
    arg1['text'] = ''
    arg2['text'] = ''
    picTestVars.width = Label(root, text = 'Width: ' + str(root.winfo_width()))
    picTestVars.width.pack()
    picTestVars.height = Label(root, text = 'Height: ' + str(root.winfo_height()))
    picTestVars.height.pack()

def showPIL(pilImage):
    w, h = root.winfo_width(), root.winfo_height()
    root.bind('<Escape>', lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tk.Canvas(root, width = w, height = h)
    canvas.pack()
    image = ImageTk.PhotoImage(pilImage)
    canvas.create_image(w/2, h/2, image = image)
    info_button = Button(root, text = 'Info', command = lambda: info(picTestVars.width, picTestVars.height))
    info_button.pack()
    root.mainloop()

pilImage = Image.open('test_1_screenshot.png')
showPIL(pilImage)
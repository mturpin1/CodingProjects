import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import NW
from PIL import Image, ImageTk
import picTestVars

root = tk.Tk()
root.geometry(picTestVars.defaultGeometry)

def clear_widgets(*widgets):
    for widget in widgets:
        widget['text'] = ''

def info(widget1, widget2):
    picTestVars.width = str(root.winfo_width())
    widget1['text'] = ('Width: ' + picTestVars.width)
    picTestVars.height = str(root.winfo_height())
    widget2['text'] = ('Height: ' + picTestVars.height)
    widget1.pack()
    widget2.pack()

def showPIL(pilImage):
    w, h = root.winfo_width(), root.winfo_height()
    root.bind('<Escape>', lambda e: (e.widget.withdraw(), e.widget.quit()))
    widthLabel = Label(root, text = '')
    heightLabel = Label(root, text = '')
    canvas = tk.Canvas(root, width = w, height = h)
    canvas.pack()
    image = ImageTk.PhotoImage(pilImage)
    canvas.create_image(w/2, h/2, image = image)
    info_button = Button(root, text = 'Info', command = lambda: [clear_widgets(widthLabel, heightLabel), info(widthLabel, heightLabel)])
    info_button.pack()
    root.mainloop()

pilImage = Image.open('test_1_screenshot.png')
showPIL(pilImage)
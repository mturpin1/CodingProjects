import sys
import tkinter as tk
from PIL import Image, ImageTk

def showPIL(pilImage):
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overridedirect(1)
    root.geometry('%dx%d+0+0' % (w, h))
    root.focus_set()
    root.bind('<Escape>', lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tk.Canvas(root, width = w, height = h)
    canvas.pack()
    canvas.configure(background = 'white')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth * ratio)
        imgHeight = int(imgHeight * ratio)
        pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2, h/2, image = image)
    root.mainloop()

pilImage = Image.open('test_1_screenshot.png')
showPIL(pilImage)
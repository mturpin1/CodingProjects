import tkinter as tk
from tkinter import END
import picTestVars

def clear_widget_text(widget):
    widget['text'] = ''

def bring_back_widget(widget):
    widget['text'] = picTestVars.textStrings[picTestVars.btnNumber]

def update_string(entry, widget):
    print(entry)
    picTestVars.btnNumber += 1
    picTestVars.textStrings.append(entry)
    widget['text'] = picTestVars.textStrings[picTestVars.btnNumber]

def label():
    root = tk.Tk()
    root.geometry(picTestVars.defaultGeometry)
    root.bind('<Escape>', lambda e: (e.widget.withdraw(), e.widget.quit()))
    label = tk.Label(root, text = picTestVars.textStrings[picTestVars.btnNumber])
    button1 = tk.Button(root, text = picTestVars.defaultClrBtnTxt, command = lambda : [clear_widget_text(label), root.focus_set()])
    button2 = tk.Button(root, text = picTestVars.defaultReviveBtnTxt, command = lambda : [bring_back_widget(label), root.focus_set()])
    userEntry = tk.Entry(root, text = 'Enter the text you want displayed. . .')
    entryButton = tk.Button(root, text = 'Print entry to terminal. . .', command = lambda : print(userEntry.get()))
    updateButton = tk.Button(root, text = picTestVars.defaultUpdateBtnTxt, command = lambda : [update_string(userEntry.get(), label), print(userEntry.get()), userEntry.delete(0, END), root.focus_set()])
    label.pack()
    button1.pack()
    button2.pack()
    userEntry.pack()
    entryButton.pack()
    updateButton.pack()
    root.mainloop()

label()
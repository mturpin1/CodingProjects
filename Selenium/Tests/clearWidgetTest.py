import tkinter as tk

def clear_widget_text(widget):
    widget['text'] = ''

if __name__ == '__main__':
    root = tk.Tk()
    label = tk.Label(root, text = 'This will be cleared.')
    button = tk.Button(root, text = 'Clear', command = lambda : clear_widget_text(label))
    label.pack()
    button.pack()
    root.mainloop()
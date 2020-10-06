import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from tkinter import Entry
from tkinter import PhotoImage
import seleniumTest

LARGEFONT = ('Verdana', 35)

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)

        self.frames = {}

        for F in (Login, Home, Settings, Confirmation):
            frame = F(container, self)

            self.frames[F] = frame

            frame.pack()

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ='Login', font = LARGEFONT)

        label.pack()

        un = StringVar()
        e1 = Entry(parent, textvariable = un)
        e1.pack()
        un.set('Your Username/Email')
        username = un.get()

        pw = StringVar()
        e2 = Entry(parent, textvariable = pw, show='*', width = 15)
        e2.pack()
        pw.set('Your Password')
        password = pw.get()


        button1 = ttk.Button(self, text ='Login', command = lambda : [controller.show_frame(Home), seleniumTest.login(username, password)])

        button1.pack()

class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ='Home', font = LARGEFONT)

        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ='Confirm Login', command = lambda : controller.show_frame(Confirmation))

        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ='Settings', command = lambda : controller.show_frame(Settings))

        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ='Settings', font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ='Home', command = lambda : controller.show_frame(Home))

        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ='Login Page', command = lambda : controller.show_frame(Login))

        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


class Confirmation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ='Confirmation', font = LARGEFONT)
        label.pack()

        canvas = tk.Canvas(parent, width = 300, height = 300)
        canvas.pack()
        img = PhotoImage(file = r'C:\Users\techies\Desktop\CodingProjects\Random Sh_t\test_2_screenshot.png')
        canvas.create_image(20, 20, image = img)

        button1 = ttk.Button(self, text ='Home', command = lambda : controller.show_frame(Home))

        button1.pack()

        button2 = ttk.Button(self, text ='Settings', command = lambda : controller.show_frame(Settings))

        button2.pack()

app = tkinterApp()
app.mainloop()
import tkinter as tk 
from tkinter import ttk 
import Test5
import Test6
import Test7
from PIL import ImageTk, Image
  
LARGEFONT =("Verdana", 35) 
   
class tkinterApp(tk.Tk): 
      
    def __init__(self, *args, **kwargs):  
          
        
        tk.Tk.__init__(self, *args, **kwargs) 
          
        
        container = tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   
        
        self.frames = {}   
   
         
        for F in (Login, Confirmation, Settings): 
   
            frame = F(container, self) 
   
            
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(Login) 
   
    
    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 
   
   
class Login(tk.Frame): 
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent) 

        label = ttk.Label(self, text ="Login", font = LARGEFONT) 
          
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10)  
   
        un = ttk.Entry(self, text = 'Username/Email')
        un.grid(row = 1, column = 1, padx = 10, pady = 10)
        Test6.username = un.get()

        pw = ttk.Entry(self, text = 'Password')
        pw.grid(row = 2, column = 1, padx = 10, pady = 10)
        Test6.password = pw.get()
        
        button1 = ttk.Button(self, text ="Login", 
        command = lambda : [controller.show_frame(Confirmation), Test5.login(Test6.username, Test6.password), Test7.printLogin()]) 
      
        
        button1.grid(row = 3, column = 1, padx = 10, pady = 10) 
   
        button2 = ttk.Button(self, text ="Settings", 
        command = lambda : [controller.show_frame(Settings), Test7.printSettings()]) 
      
        
        button2.grid(row = 4, column = 1, padx = 10, pady = 10) 
   
           
   
   
class Confirmation(tk.Frame): 
      
    def __init__(self, parent, controller): 

        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Confirmation", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 

        button1 = ttk.Button(self, text ="Login", 
                            command = lambda : [controller.show_frame(Login), Test7.printLogin()]) 
      
    
        button1.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
        button2 = ttk.Button(self, text ="Settings", 
                            command = lambda : [controller.show_frame(Settings), Test7.printSettings()]) 
      
       
        button2.grid(row = 3, column = 1, padx = 10, pady = 10) 

        print (Test6.username)
        print (Test6.password)

        if Test6.imageCreation == True:
            canvas = tk.Canvas(self, width = 300, height = 300)
            canvas.grid(column = 1, row = 1)
            img = ImageTk.PhotoImage(Image.open(r'C:\Users\techies\Desktop\CodingProjects\Random Sh_t\image-' + str(Test6.date_string) + '.png'))
            canvas.create_image(20, 20, image = img)
            Test7.printImage()
        elif Test6.imageCreation == False:
            return

   
   
   
   
class Settings(tk.Frame):  
    def __init__(self, parent, controller): 

        print('Settings Frame Selected')

        tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Settings", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   
        
        button1 = ttk.Button(self, text ="Login", 
                            command = lambda : [controller.show_frame(Login), Test7.printLogin()]) 
      
        
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
   
       
        button2 = ttk.Button(self, text ="Confirmation", 
                            command = lambda : [controller.show_frame(Confirmation), Test7.printConfirmation()]) 
      
        
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
   
app = tkinterApp() 
app.mainloop() 
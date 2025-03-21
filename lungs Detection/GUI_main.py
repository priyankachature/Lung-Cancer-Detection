

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
#project title 
root.title("Lungs Cancer Detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image main pages 
image2 = Image.open('L2.png')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)





################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%





def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
  
def window():
  root.destroy()

image2 = Image.open('logo.jpg')
image2 = image2.resize((100, 100), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=200, y=150) 



button1 = tk.Button(root, text="Login", command=log, width=15, height=1,font=('times', 17, ' bold '), bg="blue", fg="white")
button1.place(x=150, y=300)

button2 = tk.Button(root, text="Registration",command=reg,width=15, height=1,font=('times', 17, ' bold '), bg="blue", fg="white")
button2.place(x=150, y=380)

button3 = tk.Button(root, text="Exit",command=window,width=15, height=1,font=('times', 17, ' bold '), bg="red", fg="white")
button3.place(x=150, y=460)

root.mainloop()

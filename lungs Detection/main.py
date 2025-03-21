# -*- coding: utf-8 -*-




import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Lungs Cancer Detection")



# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# main pages 
image2 = Image.open('L!.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%







def log():
    from subprocess import call
    call(["python","GUI_Master.py"])


  
def window():
  root.destroy()


button1 = tk.Button(root, text="Cancer Detection", command=log, width=15, height=1,font=('times', 20, ' bold '), bg="brown", fg="white")
button1.place(x=60, y=170)



button3 = tk.Button(root, text="Exit",command=window,width=15, height=1,font=('times', 20, ' bold '), bg="Red", fg="white")
button3.place(x=60, y=270)

root.mainloop()

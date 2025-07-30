from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk") 
        
        title_lbl = Label(self.root, text="HELP DESK", font=("arial", 25, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=47)
        # top image
        img_top = Image.open(r"Project_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photo_left)        
        f_lbl.place(x=0, y=55, width=1530, height=720)  
        
        help_label = Label(f_lbl, text="For Any Query, Contact Us Below", font=("times new roman", 12, "bold"), bg="white")
        help_label.place(x=600, y=180)
        help_label = Label(f_lbl, text="Email: himanshujnp75@gmail.com", font=("times new roman", 12, "bold"), bg="white")
        help_label.place(x=600, y=230)                

if __name__ == "__main__":
        root=Tk()
        obj=Help(root)
        root.mainloop()
   
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer") 
        
        title_lbl = Label(self.root, text="DEVELOPER", font=("arial", 25, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=47)
        # top image
        img_top = Image.open(r"Project_images\dev.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photo_left)        
        f_lbl.place(x=0, y=55, width=1530, height=720)  
       
        main_frame = Frame(f_lbl, bd=2, bg="white")        
        main_frame.place(x=1020, y=0, width=500, height=600)  
        img_r = Image.open(r"Project_images\Himanshu pohto.png")
        img_r = img_r.resize((200, 200), Image.LANCZOS)
        self.photo_right = ImageTk.PhotoImage(img_r)
        f_lbl = Label(main_frame, image=self.photo_right)
        f_lbl.place(x=300, y=0, width=200, height=200)
      
       # developer info
        dev_label = Label(main_frame, text="Himanshu Yadav", font=("times new roman", 12, "bold"), bg="white")
        dev_label.place(x=0, y=5)
        dev_label = Label(main_frame, text="Student", font=("times new roman", 12, "bold"), bg="white")
        dev_label.place(x=0, y=40)
        
        img2= Image.open(r"Project_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2 = img2.resize((500, 390), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(main_frame, image=self.photo2)
        f_lbl.place(x=0, y=210, width=500, height=390)
        


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
        
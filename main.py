from tkinter import *
from tkinter import ttk
from tkinter import Toplevel
import tkinter.messagebox as msgbox
from time import strftime
from PIL import Image,ImageTk
from student import Student
from attendance import Attendance
import os
from train import Train
from developer import Developer
from help import Help
from face_recognition import Face_Recognition 
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        # first image
        try:
            img =Image.open(r"Project_images\bg image.jpg")
            img = img.resize((530,130),Image.LANCZOS)
            self.photo=ImageTk.PhotoImage(img)
            f_lbl=Label(self.root,image=self.photo)
        except:
            f_lbl=Label(self.root,text="Image 1",bg="lightgray")
        f_lbl.place(x=0,y=0,width=530,height=130)
        
        # Second image
        try:
            img1 =Image.open(r"Project_images\facialrecognition.png")
            img1 = img1.resize((530,130),Image.LANCZOS)
            self.photo1=ImageTk.PhotoImage(img1)
            f_lbl=Label(self.root,image=self.photo1)
        except:
            f_lbl=Label(self.root,text="Face Recognition",bg="lightblue")
        f_lbl.place(x=530,y=0,width=530,height=130)
        
        # third image
        try:
            img2 =Image.open(r"Project_images\bg image.jpg")
            img2 = img2.resize((530,130),Image.LANCZOS)
            self.photo2=ImageTk.PhotoImage(img2)
            f_lbl=Label(self.root,image=self.photo2)
        except:
            f_lbl=Label(self.root,text="Image 3",bg="lightgreen")
        f_lbl.place(x=1060,y=0,width=530,height=130)
        
        #bg image
        try:
            img3 =Image.open(r"Project_images\bg image.jpg")
            img3 = img3.resize((1530,710),Image.LANCZOS)
            self.photo3=ImageTk.PhotoImage(img3)
            bg_img=Label(self.root,image=self.photo3)
        except:
            bg_img=Label(self.root,bg="white")
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl =Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM", font=("arial",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height= 45)
        #==============time===============
        def time():
           string = strftime('%H:%M:%S %p')
           lbl.config(text = string)
           lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('times new roman',14,'bold'),background = 'white', foreground = 'blue')
        lbl.place(x=0,y=(-15),width=110,height=50)

        time()
     #------------------------------------------------------------------------------------------------------------------------   
 #============ student button ===========
        try:
            img4 =Image.open(r"Project_images\student.jpg")
            img4 = img4.resize((220,220),Image.LANCZOS)
            self.photo4=ImageTk.PhotoImage(img4)
            b1 = Button(bg_img,image=self.photo4, command=self.student_details,cursor="hand2")
        except:
            b1 = Button(bg_img,text="Student Image", command=self.student_details,cursor="hand2",bg="lightcoral")
        b1.place(x=200,y=70,width=220,height=220)
        
        b1_1 = Button(bg_img,text="STUDENT DETAILS",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=280,width=220,height=40)
 #============ Face Detector button ===========
        try:
            img5 =Image.open(r"Project_images\face_detector1.jpg")
            img5 = img5.resize((220,220),Image.LANCZOS)
            self.photo5=ImageTk.PhotoImage(img5)
            b2 = Button(bg_img,image=self.photo5,cursor="hand2",command=self.face_data)
        except:
            b2 = Button(bg_img,text="Face\nDetector",cursor="hand2",command=self.face_data,bg="lightsteelblue")
        b2.place(x=500,y=70,width=220,height=220)

        b2_1 = Button(bg_img,text="FACE DETACTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=280,width=220,height=40)
 #============ Attendance button ===========
        try:
            img6 =Image.open(r"Project_images\attendance.jpg")
            img6 = img6.resize((220,220),Image.LANCZOS)
            self.photo6=ImageTk.PhotoImage(img6)
            b3 = Button(bg_img,image=self.photo6,cursor="hand2",command=self.attendance)
        except:
            b3 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,bg="lightsteelblue")
        b3.place(x=800,y=70,width=220,height=220)

        b2_2 = Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2.place(x=800,y=280,width=220,height=40)
#============ help desk button =============
        try:
            img7 =Image.open(r"Project_images\help desk.jpg")
            img7 = img7.resize((220,220),Image.LANCZOS)
            self.photo7=ImageTk.PhotoImage(img7)
            b4 = Button(bg_img,image=self.photo7,cursor="hand2",command=self.help_desk)
        except:
            b4 = Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_desk,bg="lightsteelblue")
        b4.place(x=1100,y=70,width=220,height=220)

        b2_3 = Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_3.place(x=1100,y=280,width=220,height=40)
#========= train data button =============
        try:
            img4_1 =Image.open(r"Project_images\Train.jpg")
            img4_1 = img4_1.resize((220,220),Image.LANCZOS)
            self.photo4_1=ImageTk.PhotoImage(img4_1)
            b1_1 = Button(bg_img,image=self.photo4_1,cursor="hand2",command=self.train_data)
        except:
            b1_1 = Button(bg_img,text="TRAIN DATA",command=self.train_data,cursor="hand2",bg="lightcoral")
        b1_1.place(x=200,y=350,width=220,height=220)
        
        b1_1_1 = Button(bg_img,text="TRAIN DATA",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1_1.place(x=200,y=550,width=220,height=40)
#============ photos face button===============
        try:
            img5_2 =Image.open(r"Project_images\sample.jpg")
            img5_2 = img5_2.resize((220,220),Image.LANCZOS)
            self.photo5_2=ImageTk.PhotoImage(img5_2)
            b2_2 = Button(bg_img,image=self.photo5_2,cursor="hand2",command=self.open_image)
        except:
            b2_2 = Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_image,bg="lightsteelblue")
        b2_2.place(x=500,y=350,width=220,height=220)

        b2_1_2 = Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_image, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1_2.place(x=500,y=550,width=220,height=40)
#============ developer button ============
        try:
            img6_3 =Image.open(r"Project_images\dev.jpg")
            img6_3 = img6_3.resize((220,220),Image.LANCZOS)
            self.photo6_3=ImageTk.PhotoImage(img6_3)
            b3_3 = Button(bg_img,image=self.photo6_3,cursor="hand2",command=self.developer)
        except:
            b3_3 = Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer,bg="lightsteelblue")
        b3_3.place(x=800,y=350,width=220,height=220)

        b2_2_3 = Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_2_3.place(x=800,y=550,width=220,height=40)
#============exit button=================
        try:
            img7_4 =Image.open(r"Project_images\exit.jpg")
            img7_4 = img7_4.resize((220,220),Image.LANCZOS)
            self.photo7_4=ImageTk.PhotoImage(img7_4)
            b4_4 = Button(bg_img,image=self.photo7_4,cursor="hand2",command=self.iExit) # Add the command=self.iExit to the button to call the iExit function when clicked.
        except:
            b4_4 = Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,bg="lightsteelblue") # Add the command=self.iExit to the button to call the iExit function when clicked.
        b4_4.place(x=1100,y=350,width=220,height=220)

        b2_3_4 = Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white") # Add the command=self.iExit to the button to call the iExit function when clicked.
        b2_3_4.place(x=1100,y=550,width=220,height=40)
    
    def open_image(self):
        os.startfile("data")
    def iExit(self):
        self.iExit = msgbox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root) # Add the parent=self.root to the msgbox to make it appear on top of the main window.
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
            
    #=========== Function Buttons ===========
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window) 
    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)       
    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)       
if __name__ == "__main__":
        root=Tk()
        obj=Face_Recognition_System(root)
        root.mainloop()
 
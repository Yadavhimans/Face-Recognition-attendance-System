from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import cv2
import os 
import csv 
mydata = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance")
    #================variables=================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
               
        # first image
        
        img = Image.open(r"Project_images\smart-attendance.jpg")
        img = img.resize((765, 200), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photo)        
        f_lbl.place(x=0, y=0, width=765, height=200) 
        
        # Second image
        
        img1 = Image.open(r"Project_images\iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((765, 200), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)        
        f_lbl = Label(self.root, image=self.photo1)        
        f_lbl.place(x=765, y=0, width=765, height=200) 
        
        # bg image
        img2 = Image.open(r"Project_images\bg.jpg")
        img2 = img2.resize((1530, 710), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root, image=self.photo2)
        bg_img.place(x=0, y=200, width=1530, height=710)
        
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("arial", 25, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=201, width=1530, height=45) 
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1510, height=600)
        #======= left label frame ========
        Left_frame = LabelFrame(main_frame, bd=2, bg="white",fg="red4", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=550)
        img3 = Image.open(r"Project_images\face-recognition.png")
        img3 = img3.resize((710, 120), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(Left_frame, image=self.photo3)
        f_lbl.place(x=10, y=0, width=700, height=120)
        
        left_inner_frame = Frame(Left_frame, bd=2, bg="white", relief=RIDGE)
        left_inner_frame.place(x=10, y=135, width=700, height=380)
#==========Labels and Entry fields==========
        # Student ID
        attendanceId_label = Label(left_inner_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.var_atten_id = StringVar()
        attendanceId_entry = ttk.Entry(left_inner_frame, textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        # Roll No
        roll_label = Label(left_inner_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W) 
        roll_entry = ttk.Entry(left_inner_frame, textvariable=self.var_atten_roll, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(left_inner_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.var_atten_name = StringVar()
        studentName_entry = ttk.Entry(left_inner_frame, textvariable=self.var_atten_name, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        dep_label = Label(left_inner_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        self.var_atten_dep = StringVar()
        dep_entry = ttk.Entry(left_inner_frame, textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inner_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.var_atten_time = StringVar()
        time_entry = ttk.Entry(left_inner_frame, textvariable=self.var_atten_time, font=("times new roman", 12, "bold"))
        time_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inner_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        self.var_atten_date = StringVar()
        date_entry = ttk.Entry(left_inner_frame, textvariable=self.var_atten_date, font=("times new roman", 12, "bold"))
        date_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Attendance Status
        attendance_label = Label(left_inner_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        self.var_atten_attendance = StringVar()
        
        attendance_combo = ttk.Combobox(left_inner_frame, textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly")
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Buttons frame
        btn_frame = Frame(left_inner_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=696, height=38)

        save_btn = Button(btn_frame, text="Import CSV",command=self.importCsv ,width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        #======= right label frame ========
        Right_frame = LabelFrame(main_frame, bd=2, bg="white",fg="red4", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=745, y=10, width=720, height=550)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=500)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # CSV format: Name,Roll,Department,Student_ID,Time,Date,Status
        # Table columns should match CSV order
        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("name", "roll", "department", "id", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("id", text="Student ID")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("name", width=120)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("department", width=120)
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
   #=================fetch data=================     
       
    def fethchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #============import csv=================        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fethchData(mydata)   
    #============export csv=================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                msgbox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                msgbox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            msgbox.showerror("Error",f"Due To : {str(es)}",parent=self.root)             
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']

       
        if len(rows) >= 7:
            self.var_atten_name.set(rows[0])      
            self.var_atten_roll.set(rows[1])    
            self.var_atten_dep.set(rows[2])    
            self.var_atten_id.set(rows[3])        
            self.var_atten_time.set(rows[4])      
            self.var_atten_date.set(rows[5])      
            self.var_atten_attendance.set(rows[6]) 
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")   
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
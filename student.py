from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import cv2
class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student detail") 
        #===============variables==================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_teacher = StringVar()
        self.var_address = StringVar()
        self.var_radio = StringVar()  # Single variable for radio buttons
        
        # Define the validation method first
        self.validate_phone_number = self.phone_validation
        
        # first image
        try:
            img = Image.open(r"Project_images\face-recognition.png")
            img = img.resize((530, 130), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            f_lbl = Label(self.root, image=self.photo)
        except Exception as e:
            f_lbl = Label(self.root, text="Image 1", bg="lightgray")
        f_lbl.place(x=0, y=0, width=530, height=130)
        
        # Second image
        try:
            img1 = Image.open(r"Project_images\iStock-182059956_18390_t12.jpg")
            img1 = img1.resize((530, 130), Image.LANCZOS)
            self.photo1 = ImageTk.PhotoImage(img1)
            f_lbl = Label(self.root, image=self.photo1)
        except Exception as e:
            f_lbl = Label(self.root, text="Face Recognition", bg="lightblue")
        f_lbl.place(x=530, y=0, width=530, height=130)
        
        # third image
        try:
            img2 = Image.open(r"Project_images\smart-attendance.jpg")
            img2 = img2.resize((530, 130), Image.LANCZOS)
            self.photo2 = ImageTk.PhotoImage(img2)
            f_lbl = Label(self.root, image=self.photo2)
        except Exception as e:
            f_lbl = Label(self.root, text="Image 3", bg="lightgreen")
        f_lbl.place(x=1060, y=0, width=530, height=130) 
        
        #bg image
        try:
            img3 = Image.open(r"Project_images\bg.jpg")
            img3 = img3.resize((1530, 710), Image.LANCZOS)
            self.photo3 = ImageTk.PhotoImage(img3)
            bg_img = Label(self.root, image=self.photo3)
        except Exception as e:
            bg_img = Label(self.root, bg="white")
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("arial", 25, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=40)
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=45, width=1515, height=615)
        
        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
        Left_frame.place(x=20, y=10, width=720, height=580)
        
        # Second image
        try:
            img_left = Image.open(r"Project_images\AdobeStock_303989091.jpeg")
            img_left = img_left.resize((710, 120), Image.LANCZOS)
            self.photo_left = ImageTk.PhotoImage(img_left)
            f_lbl = Label(Left_frame, image=self.photo_left)
        except Exception as e:
            f_lbl = Label(Left_frame, text="Student Image", bg="lightgray")
        f_lbl.place(x=10, y=0, width=700, height=120)
        
        # current course information
        current_course_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=20, y=160, width=720, height=130)
        
        #department
        dep_lbl = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_lbl.grid(row=0, column=0, padx=10, sticky=W)
        
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=20, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        #course
        course_labl = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_labl.grid(row=0, column=2, padx=10, sticky=W)
        
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)
        
        #year
        year_labl = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_labl.grid(row=1, column=0, padx=10, sticky=W)
        
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=20, state="readonly")
        year_combo["values"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)
        
        #semester
        sem_labl = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_labl.grid(row=1, column=2, padx=10, sticky=W)
        
        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=20, state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        
        #class student information
        class_student_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=20, y=290, width=720, height=320)
        
        #student id
        stu_id_labl = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        stu_id_labl.grid(row=0, column=0, padx=10, sticky=W)
        
        stu_id_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        stu_id_entry.grid(row=0, column=1, padx=10, sticky=W)
        
        #student name
        stu_name_labl = Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        stu_name_labl.grid(row=0, column=2, padx=10, sticky=W)
        
        stu_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        stu_name_entry.grid(row=0, column=3, padx=10, sticky=W)
        
        #student roll no
        stu_roll_labl = Label(class_student_frame, text="Roll No", font=("times new roman", 12, "bold"), bg="white")
        stu_roll_labl.grid(row=1, column=0, padx=10, sticky=W)
        
        stu_roll_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        stu_roll_entry.grid(row=1, column=1, padx=10, sticky=W)
        
        #gender
        gender_labl = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_labl.grid(row=1, column=2, padx=10, sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=20, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)   
        
        #dob
        dob_labl = Label(class_student_frame, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        dob_labl.grid(row=2, column=0, padx=10, sticky=W)
        
        dob_entry = DateEntry(class_student_frame, textvariable=self.var_dob, width=18, font=("times new roman", 12, "bold"),
                      background="darkblue", foreground="white", borderwidth=2, date_pattern='yyyy-mm-dd')
        dob_entry.grid(row=2, column=1, padx=10, sticky=W)     
        
        #email
        email_labl = Label(class_student_frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
        email_labl.grid(row=2, column=2, padx=10, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=2, column=3, padx=10, sticky=W)
        
        #phone no - only numeric values
        phone_labl = Label(class_student_frame, text="Phone No", font=("times new roman", 12, "bold"), bg="white")
        phone_labl.grid(row=3, column=0, padx=10, pady=5, sticky=W)   
        
        # Register validation function
        validate_phone = self.root.register(self.validate_phone_number)     
        
        # Create entry with validation
        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"), 
                               validate="key", 
                               validatecommand=(validate_phone, '%P'))
        phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)      
        
        #teacher name   
        teacher_labl = Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacher_labl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        
        #address
        address_labl = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        address_labl.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
        #radio buttons - using a single variable
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        
        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1, padx=10, pady=10, sticky=W)
        
        #buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)
        
        #save button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
        
        #update button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
        
        #delete button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)
        
        #reset button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        
        btn_frame2 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=0, y=235, width=715, height=35)
        
        #take photo sample button
        take_photo_btn = Button(btn_frame2,command=self.generate_dataset, text="Take Photo Sample", width=39, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0)
        
        #upload photo sample button
        update_photo_btn = Button(btn_frame2, text="Update Photo Sample", width=39, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=1)
        
        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=720, height=580)
        
        # Right frame image
        try:
            img_right = Image.open(r"Project_images\student.jpg")
            img_right = img_right.resize((710, 120), Image.LANCZOS)
            self.photo_right = ImageTk.PhotoImage(img_right)
            f_lbl = Label(Right_frame, image=self.photo_right)
        except Exception as e:
            f_lbl = Label(Right_frame, text="Student Image", bg="lightgray")
        f_lbl.place(x=10, y=0, width=700, height=120)
        
        #============ Search System ===========
        #search frame
        search_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Search Student", font=("times new roman", 12, "bold"))
        search_frame.place(x=770, y=160, width=700, height=75)        
        
        #search label
        search_labl = Label(search_frame, text="Search By", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_labl.grid(row=0, column=0, padx=10, sticky=W)        
        
        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=20, state="readonly")
        search_combo["values"] = ("Select Option", "Roll No", "Phone No", "Student ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        #search entry
        search_entry = ttk.Entry(search_frame, width=16, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=7,  sticky=W)
        #search button
        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=7)
        #show all button
        showall_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.fetch_data)
        showall_btn.grid(row=0,column=4,padx=7)
        #table frame
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=8,y=212,width=700,height=340)
        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","roll","gender","dob","email","phone","teacher","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
   #==================function declaration==================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            msgbox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Admin@1402",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_teacher.get(),
                    self.var_address.get(),
                    self.var_radio.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                msgbox.showinfo("Success","Student details has been added successfully",parent=self.root)    
            except Exception as es:
                msgbox.showerror("Error",f"Error due to {str(es)}",parent=self.root) 
                
    #============ fetch data ===========
    def fetch_data(self):
 
            conn=mysql.connector.connect(host="localhost",username="root",password="Admin@1402",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()    
            conn.close()    
    #=========== get cursor ===========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_roll.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])
        self.var_teacher.set(data[11])
        self.var_address.set(data[12])
        self.var_radio.set(data[13])
    #=========== update function ===========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            msgbox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update = msgbox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Admin@1402",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Teacher=%s, Address=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                                  self.var_dep.get(),
                                                                                                                  self.var_course.get(),
                                                                                                                  self.var_year.get(),
                                                                                                                  self.var_semester.get(),
                                                                                                                  self.var_std_name.get(),
                                                                                                                  self.var_roll.get(),
                                                                                                                  self.var_gender.get(),
                                                                                                                  self.var_dob.get(),
                                                                                                                  self.var_email.get(),
                                                                                                                  self.var_phone.get(),
                                                                                                                  self.var_teacher.get(),
                                                                                                                  self.var_address.get(),
                                                                                                                  self.var_radio.get(),
                                                                                                                  self.var_std_id.get()
                                                                                                              ))
                else:
                    if not Update:
                        return                     
                msgbox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                    
            except Exception as es:
                msgbox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                    
    #============ delete function ===========
    def delete_data(self):
        if self.var_std_id.get()=="":
            msgbox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete = msgbox.askyesno("Delete","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Admin@1402",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                msgbox.showinfo("Delete","Student details deleted successfully",parent=self.root)
            except Exception as es:
                msgbox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
 
     #============ reset function ===========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_teacher.set("")
        self.var_address.set("")
        self.var_radio.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio.set("")
        
    #============ generate data set or take photo samples ============
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            msgbox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                # First, save/update the student data
                conn=mysql.connector.connect(host="localhost",username="root",password="Admin@1402",database="face_recognizer")
                my_cursor=conn.cursor()

                # Check if student already exists
                my_cursor.execute("select * from student where Student_id=%s", (self.var_std_id.get(),))
                existing_student = my_cursor.fetchone()

                if existing_student:
                    # Update existing student
                    print(f"Updating existing student with ID: {self.var_std_id.get()}")
                else:
                    # Add new student
                    print(f"Adding new student with ID: {self.var_std_id.get()}")
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_teacher.get(),
                        self.var_address.get(),
                        self.var_radio.get()
                    ))

                # Use the actual student ID for photos
                student_id = self.var_std_id.get()
                # Update the student record to mark that photos will be taken
                my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Teacher=%s, Address=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                                  self.var_dep.get(),
                                                                                                                  self.var_course.get(),
                                                                                                                  self.var_year.get(),
                                                                                                                  self.var_semester.get(),
                                                                                                                  self.var_std_name.get(),
                                                                                                                  self.var_roll.get(),
                                                                                                                  self.var_gender.get(),
                                                                                                                  self.var_dob.get(),
                                                                                                                  self.var_email.get(),
                                                                                                                  self.var_phone.get(),
                                                                                                                  self.var_teacher.get(),
                                                                                                                  self.var_address.get(),
                                                                                                                  "Yes",  # PhotoSample = Yes
                                                                                                                  self.var_std_id.get()
                                                                                                              ))

                conn.commit()
                self.fetch_data()
                conn.close()

                # Confirm data is saved
                print(f"Student data saved successfully for ID: {student_id}")
                print(f"Student Name: {self.var_std_name.get()}")
                print(f"Department: {self.var_dep.get()}")
                print(f"Roll: {self.var_roll.get()}")

                # Create data directory if it doesn't exist
                import os
                if not os.path.exists("data"):
                    os.makedirs("data")

                # Load predefined data on frontal faces from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                # Check if classifier loaded successfully
                if face_classifier.empty():
                    msgbox.showerror("Error", "Could not load face classifier. Please check OpenCV installation.", parent=self.root)
                    return

                def face_cropped(img):
                    # Convert image to grayscale
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor 1.3
                    # Minimum neighbor = 5
                    if len(faces) > 0:
                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                    return None

                # Initialize camera - try different camera indices and backends
                cap = None
                camera_indices = [1, 0, 2]  # Try camera 1 first (known working), then others
                backends = [cv2.CAP_DSHOW, cv2.CAP_ANY]  # Use DSHOW first for Windows

                for cam_idx in camera_indices:
                    for backend in backends:
                        try:
                            print(f"Trying camera {cam_idx} with backend {backend}")
                            cap = cv2.VideoCapture(cam_idx, backend)
                            if cap.isOpened():
                                # Set properties before testing
                                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                                cap.set(cv2.CAP_PROP_FPS, 30)
                                cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

                                # Test if we can read a frame
                                ret, test_frame = cap.read()
                                if ret and test_frame is not None:
                                    print(f"✓ Camera {cam_idx} working with backend {backend}")
                                    print(f"Frame shape: {test_frame.shape}")
                                    break
                                else:
                                    print(f"✗ Camera {cam_idx} opened but cannot read frames")
                                    cap.release()
                                    cap = None
                            else:
                                print(f"✗ Cannot open camera {cam_idx} with backend {backend}")
                        except Exception as e:
                            print(f"✗ Error with camera {cam_idx}, backend {backend}: {e}")
                            if cap:
                                cap.release()
                            cap = None
                            continue
                    if cap is not None:
                        break

                # Check if camera opened successfully
                if cap is None or not cap.isOpened():
                    msgbox.showerror("Error", "Could not open camera. Please check if:\n1. Camera is connected\n2. Camera is not being used by another application\n3. Camera drivers are installed properly\n4. Try closing other camera applications", parent=self.root)
                    return

                img_id=0
                capture_counter = 0  # Counter to control capture rate
                msgbox.showinfo("Info", f"Camera will open now for:\n\nStudent ID: {student_id}\nName: {self.var_std_name.get()}\nDepartment: {self.var_dep.get()}\n\nInstructions:\n- Position your face in the camera\n- Camera will auto-capture when face is detected\n- Press ESC to stop\n- 100 samples will be captured automatically", parent=self.root)

                # Give camera time to initialize
                import time
                time.sleep(1)

                frame_count = 0
                failed_frames = 0

                while True:
                    ret, my_frame = cap.read()
                    frame_count += 1

                    # Check if frame was read successfully
                    if not ret or my_frame is None:
                        failed_frames += 1
                        print(f"Failed to read frame {frame_count}, failed frames: {failed_frames}")
                        if failed_frames > 10:  # Too many failed frames
                            msgbox.showerror("Error", "Camera stopped working. Please try again.", parent=self.root)
                            break
                        continue

                    # Reset failed frame counter on successful read
                    failed_frames = 0

                    # Check if frame has valid data
                    if my_frame.shape[0] == 0 or my_frame.shape[1] == 0:
                        print("Invalid frame dimensions")
                        continue

                    # Create a copy for display
                    display_frame = my_frame.copy()

                    # Get cropped face
                    cropped_face = face_cropped(my_frame)

                    if cropped_face is not None:
                        # Draw rectangle around detected face on display frame
                        gray = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

                        # Control capture rate - capture every 3 frames when face is detected
                        capture_counter += 1
                        if capture_counter % 3 == 0:  # Capture every 3rd frame
                            img_id += 1
                            face = cv2.resize(cropped_face, (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)

                        # Show status and student info on display frame
                        cv2.putText(display_frame, f"Capturing: {img_id}/100", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(display_frame, "Face Detected!", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(display_frame, f"Student ID: {student_id}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                        cv2.putText(display_frame, f"Name: {self.var_std_name.get()}", (10, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    else:
                        # Show message when no face detected
                        cv2.putText(display_frame, "Position your face in the camera", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        cv2.putText(display_frame, f"Samples captured: {img_id}/100", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                        cv2.putText(display_frame, f"Student ID: {student_id}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                        cv2.putText(display_frame, f"Name: {self.var_std_name.get()}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                    # Show instructions
                    cv2.putText(display_frame, "Press ESC to stop", (10, display_frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                    # Display the frame
                    try:
                        cv2.imshow("Face Recognition - Photo Capture", display_frame)
                    except Exception as e:
                        print(f"Error displaying frame: {e}")
                        continue

                    # Check for key presses
                    key = cv2.waitKey(1) & 0xFF
                    if key == 27 or int(img_id) >= 100:  # ESC key or 100 samples
                        break

                cap.release()
                cv2.destroyAllWindows()

                if img_id > 0:
                    msgbox.showinfo("Result", f"Dataset generation completed!\n\nStudent ID: {student_id}\nName: {self.var_std_name.get()}\nSamples captured: {img_id}\n\nPhotos saved in 'data' folder with naming:\nuser.{student_id}.1.jpg to user.{student_id}.{img_id}.jpg", parent=self.root)
                    print(f"Photos saved for Student ID {student_id}: {img_id} samples")
                else:
                    msgbox.showwarning("Warning", f"No face samples were captured for Student ID: {student_id}\nName: {self.var_std_name.get()}\n\nPlease try again with better lighting.", parent=self.root)

            except Exception as es:
                msgbox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
 # Validate phone number
    def phone_validation(self, insert_text):
        """Validate that input contains only digits and is not longer than 10 characters"""
        # Check if input is empty or contains only digits
        if insert_text == "" or insert_text.isdigit():
            # Check if length is not more than 10
            if len(insert_text) <= 10:
                return True
        return False
    
    
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

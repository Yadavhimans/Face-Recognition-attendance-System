from tkinter import *
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk
from datetime import datetime
import cv2
import mysql.connector
import os
import time

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.last_attendance_time = {}  # Track last attendance time for each student ID
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("arial", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=47)

        # First image
        img_left = Image.open(r"Project_images\face_detector1.jpg")
        img_left = img_left.resize((650, 700), Image.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(self.root, image=self.photo_left)
        f_lbl_left.place(x=0, y=55, width=650, height=700)


        # Second image
        img_right = Image.open(r"Project_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_right = img_right.resize((950, 700), Image.LANCZOS)
        self.photo_right = ImageTk.PhotoImage(img_right)
        f_lbl_right = Label(self.root, image=self.photo_right)
        f_lbl_right.place(x=650, y=55, width=950, height=700)

        # Face Recognition Button
        Button(self.root, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2",
               font=("times new roman", 15, "bold"), bg="darkgreen", fg="white").place(x=1012, y=680, width=220, height=41)
#===============Attendance=================
    def mark_attendance(self, n, r, d, id):
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        current_timestamp = time.time()

        # Check if we recently marked attendance for this person (prevent rapid duplicates)
        if id in self.last_attendance_time:
            time_diff = current_timestamp - self.last_attendance_time[id]
            if time_diff < 10:  # Wait at least 10 seconds between markings

                return

        # Check if attendance file exists, if not create with header
        if not os.path.exists("attendance.csv"):
            with open("attendance.csv", "w", newline="") as f:
                f.write("Name,Roll,Department,Student_ID,Time,Date,Status\n")

        # Read existing attendance records to check if already marked today
        try:
            with open("attendance.csv", "r") as f:
                lines = f.readlines()
                for line in lines[1:]:  # Skip header
                    if line.strip():  # Skip empty lines
                        parts = line.strip().split(",")
                        if len(parts) >= 6:
                            # Check if this person already marked attendance today
                            record_date = parts[5]  # Date column
                            record_id = parts[3]    # Student_ID column
                            if record_date == current_date and record_id == id:

                                return  # Don't mark again
        except FileNotFoundError:
            pass  # File doesn't exist yet, will be created

        # Mark new attendance
        with open("attendance.csv", "a", newline="") as f:
            f.write(f"{n},{r},{d},{id},{current_time},{current_date},Present\n")
            self.last_attendance_time[id] = current_timestamp  # Update last marking time

    def build_dynamic_id_mapping(self):
        """Build ID mapping dynamically based on current database and available photos"""
        try:
            import os
            import glob
            from collections import Counter

            # Get all students from database
            conn = mysql.connector.connect(host="localhost", username="root", password="Admin@1402", database="face_recognizer")
            cursor = conn.cursor()
            cursor.execute("SELECT Student_id, Name FROM student")
            db_students = {str(row[0]): row[1] for row in cursor.fetchall()}
            conn.close()

            # Get available photo IDs
            if not os.path.exists("data"):
                print("No data folder found")
                return {}

            photo_files = glob.glob("data/user.*.*.jpg")
            photo_ids = {}
            for photo_file in photo_files:
                try:
                    filename = os.path.basename(photo_file)
                    parts = filename.split('.')
                    if len(parts) >= 4 and parts[0] == "user":
                        student_id = parts[1]
                        if student_id not in photo_ids:
                            photo_ids[student_id] = 0
                        photo_ids[student_id] += 1
                except:
                    continue

            # Build mapping: photo_id -> database_id (only for students that exist in both)
            id_mapping = {}
            matched_students = []
            unmatched_photos = []
            unmatched_db = []

            for photo_id in photo_ids:
                # Convert photo_id to string for database comparison
                photo_id_str = str(photo_id)
                if photo_id_str in db_students:
                    # Map training ID (int) to database ID (int)
                    id_mapping[int(photo_id)] = int(photo_id_str)  # Direct mapping
                    matched_students.append(f"ID {photo_id}: {db_students[photo_id_str]} ({photo_ids[photo_id]} photos)")
                else:
                    unmatched_photos.append(f"ID {photo_id}: {photo_ids[photo_id]} photos (NO DATABASE ENTRY)")

            for db_id in db_students:
                # Convert db_id to string for photo comparison
                if db_id not in photo_ids:
                    unmatched_db.append(f"ID {db_id}: {db_students[db_id]} (NO PHOTOS)")

            print(f"Face recognition ready: {len(matched_students)} students loaded")
            if unmatched_db:
                print(f"Note: {len(unmatched_db)} students need photos to be taken")
            if unmatched_photos:
                print(f"Note: {len(unmatched_photos)} photo sets have no database entries")

            return id_mapping

        except Exception as e:
            print(f"Error building ID mapping: {e}")
            return {}

    def check_and_retrain_model(self, available_photo_ids):
        """Check if model needs retraining and retrain if necessary"""
        try:
            import os

            # Check if classifier exists and get its modification time
            classifier_path = "classifier.xml"
            data_dir = "data"

            needs_retraining = False

            if not os.path.exists(classifier_path):
                print("No classifier found. Training new model...")
                needs_retraining = True
            else:
                # Check if any photos are newer than the classifier
                classifier_time = os.path.getmtime(classifier_path)
                for photo_file in os.listdir(data_dir):
                    if photo_file.endswith('.jpg'):
                        photo_path = os.path.join(data_dir, photo_file)
                        if os.path.getmtime(photo_path) > classifier_time:
                            print("New photos detected. Retraining model...")
                            needs_retraining = True
                            break

            if needs_retraining:
                self.train_face_model()

        except Exception as e:
            print(f"Error checking model: {e}")

    def train_face_model(self):
        """Train the face recognition model with all available photos"""
        try:
            import os
            import cv2
            import numpy as np
            from PIL import Image

            data_dir = "data"
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

            if len(path) == 0:
                print("No photos found for training")
                return False

            faces = []
            ids = []

            print(f"Training model with {len(path)} photos...")

            for image_path in path:
                try:
                    img = Image.open(image_path).convert('L')
                    imageNp = np.array(img, 'uint8')
                    filename = os.path.split(image_path)[1]
                    parts = filename.split('.')
                    if len(parts) >= 3:
                        id = int(parts[1])
                        faces.append(imageNp)
                        ids.append(id)
                except Exception as e:
                    print(f"Error processing {image_path}: {e}")
                    continue

            if len(faces) == 0:
                print("No valid face images found")
                return False

            ids = np.array(ids)
            unique_ids = sorted(set(ids))

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")

            print(f"Model trained: {len(faces)} images, {len(unique_ids)} students")

            return True

        except Exception as e:
            print(f"Error training model: {e}")
            return False

#==========Face Recognition Function==========
    def face_recog(self):
        # Dynamic ID mapping: Get current students from database and match with available photos
        id_mapping = self.build_dynamic_id_mapping()

        if not id_mapping:
            msgbox.showerror("Error", "No students found in database or no photos available. Please add students and take photos first.")
            return



        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Use more sensitive parameters for better face detection
            # Reduced minSize and adjusted parameters for better detection
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors, minSize=(50, 50), maxSize=(300, 300))
            cord = []



            for (x, y, w, h) in features:
                training_id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))

                # Map training ID to database ID
                database_id = id_mapping.get(training_id, None)



                # Debug: Show what we detected
                print(f"Detected: Training_ID={training_id}, Confidence={confidence}%, Mapped_DB_ID={database_id}")

                # Stricter confidence threshold to avoid false positives
                if confidence > 75 and database_id is not None:
                    try:
                        # Connect to database
                        conn = mysql.connector.connect(host="localhost", username="root", password="Admin@1402", database="face_recognizer")
                        my_cursor = conn.cursor()

                        # Get student details using the mapped database ID
                        my_cursor.execute("select Name from student where Student_id="+str(database_id))
                        n_result = my_cursor.fetchone()

                        my_cursor.execute("select Roll from student where Student_id="+str(database_id))
                        r_result = my_cursor.fetchone()

                        my_cursor.execute("select Dep from student where Student_id="+str(database_id))
                        d_result = my_cursor.fetchone()

                        my_cursor.execute("select Student_id from student where Student_id="+str(database_id))
                        id_result = my_cursor.fetchone()

                        # Close database connection
                        conn.close()

                        # Check if student exists in database
                        if n_result and r_result and d_result and id_result:
                            # Known student - green rectangle
                            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

                            n = "+".join(n_result)
                            r = "+".join(r_result)
                            d = "+".join(d_result)
                            student_id = "+".join(id_result)

                            # Display student information
                            cv2.putText(img, f"ID: {student_id}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Name: {n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Roll: {r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                            cv2.putText(img, f"Dept: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                            # Mark attendance ONLY for known students
                            self.mark_attendance(n, r, d, student_id)
                        else:
                            # Student not found in database - red rectangle
                            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                            cv2.putText(img, "Unknown Student", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)


                    except Exception as e:
                        # Database error - red rectangle
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "DB Error", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                elif confidence > 60 and database_id is None:
                    # Training ID not in our mapping - red rectangle
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unmapped ID {training_id}", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                else:
                    # Low confidence face - red rectangle
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, f"Low Conf {confidence}%", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)


                cord = [x, y, w, h]

            return cord
        def recognize(img, clf, faceCascade):
            # Use better parameters for face detection: more sensitive settings
            cord = draw_boundary(img, faceCascade, 1.1, 3, (255, 255, 255), "Face", clf)
            return img

        # Load face cascade classifier
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        if faceCascade.empty():
            msgbox.showerror("Error", "Could not load haarcascade_frontalface_default.xml file")
            return

        # Load trained classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        try:
            clf.read("classifier.xml")
            print("✅ Face recognition model loaded successfully")

            # Check what IDs the model knows about
            import os
            if os.path.exists("data"):
                data_files = [f for f in os.listdir("data") if f.endswith('.jpg')]
                if data_files:
                    sample_ids = set()
                    for f in data_files[:10]:  # Check first 10 files
                        try:
                            parts = f.split('.')
                            if len(parts) >= 3:
                                sample_ids.add(int(parts[1]))
                        except:
                            continue
                    print(f"Model trained on sample IDs: {sorted(sample_ids)}")

        except Exception as e:
            msgbox.showerror("Error", f"Could not load classifier.xml file: {str(e)}")
            return

        # Initialize camera - try different camera indices and backends (same as student.py)
        video_capture = None
        camera_indices = [1, 0, 2]  # Try camera 1 first (known working), then others
        backends = [cv2.CAP_DSHOW, cv2.CAP_ANY]  # Use DSHOW first for Windows

        for cam_idx in camera_indices:
            for backend in backends:
                try:
                    print(f"Trying camera {cam_idx} with backend {backend}")
                    video_capture = cv2.VideoCapture(cam_idx, backend)
                    if video_capture.isOpened():
                        # Set properties before testing
                        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                        video_capture.set(cv2.CAP_PROP_FPS, 30)
                        video_capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)

                        # Test if we can read a frame
                        ret, test_frame = video_capture.read()
                        if ret and test_frame is not None:
                            print(f"✓ Camera {cam_idx} working with backend {backend}")
                            print(f"Frame shape: {test_frame.shape}")
                            break
                        else:
                            print(f"✗ Camera {cam_idx} opened but cannot read frames")
                            video_capture.release()
                            video_capture = None
                    else:
                        print(f"✗ Cannot open camera {cam_idx} with backend {backend}")
                except Exception as e:
                    print(f"✗ Error with camera {cam_idx}, backend {backend}: {e}")
                    if video_capture:
                        video_capture.release()
                    video_capture = None
                    continue
            if video_capture is not None:
                break

        # Check if camera opened successfully
        if video_capture is None or not video_capture.isOpened():
            msgbox.showerror("Error", "Could not open any camera. Please check if camera is connected and not being used by another application.")
            return

        print("Camera opened successfully. Press 'Enter' or 'q' to exit.")
        print("Face detection parameters: scaleFactor=1.3, minNeighbors=5, minSize=(30,30)")

        while True:
            ret, img = video_capture.read()
            if not ret:
                print("Failed to read frame from camera")
                msgbox.showerror("Error", "Failed to read from camera")
                break

            
            img = recognize(img, clf, faceCascade)

            
            cv2.imshow("Face Recognition System - Press Enter to Exit", img)

            
            key = cv2.waitKey(1) & 0xFF
            if key == 13 or key == ord('q'): 
                print("Face recognition stopped by user")
                break

        video_capture.release()
        cv2.destroyAllWindows()
        print("Camera closed successfully.")
    
       
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()          
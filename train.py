from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import cv2
import numpy as np
import os
class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data Set")  # Change the title to "Train Data Set"
        
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("arial", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=47)
        # top image
        img_top = Image.open(r"Project_images\facialrecognition.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photo_left = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photo_left)        
        f_lbl.place(x=0, y=55, width=1530, height=325)  
       
        # button
        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier, cursor="hand2",font=("times new roman",30,"bold"),bg="darkblue",fg="white")
        b1.place(x=0,y=380,width=1530,height=57)
        #bottom image
        img_bottom = Image.open(r"Project_images\opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photo_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photo_bottom)        
        f_lbl.place(x=0, y=438, width=1530, height=325)  
    def train_classifier(self):
        try:
            data_dir = "data"

            # Check if data directory exists
            if not os.path.exists(data_dir):
                msgbox.showerror("Error", "Data directory not found! Please capture some face samples first.", parent=self.root)
                return

            # Get all image files
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

            if len(path) == 0:
                msgbox.showerror("Error", "No image files found in data directory! Please capture some face samples first.", parent=self.root)
                return

            faces = []
            ids = []

            msgbox.showinfo("Info", f"Found {len(path)} images. Starting training process...", parent=self.root)

            for image_path in path:
                try:
                    # Open and convert image to grayscale
                    img = Image.open(image_path).convert('L')
                    imageNp = np.array(img, 'uint8')

                    # Extract ID from filename (format: user.ID.number.jpg)
                    filename = os.path.split(image_path)[1]
                    parts = filename.split('.')

                    if len(parts) < 3:
                        print(f"Skipping invalid filename: {filename}")
                        continue

                    id = int(parts[1])  # Extract the ID part

                    faces.append(imageNp)
                    ids.append(id)

                    # Show training progress
                    cv2.imshow("Training", imageNp)
                    cv2.waitKey(1)

                except Exception as e:
                    print(f"Error processing {image_path}: {e}")
                    continue

            cv2.destroyAllWindows()

            if len(faces) == 0:
                msgbox.showerror("Error", "No valid face images found! Please check your image files.", parent=self.root)
                return

            # Convert ids to numpy array
            ids = np.array(ids)

            msgbox.showinfo("Info", f"Processing {len(faces)} face samples for training...", parent=self.root)

            # Check if OpenCV face module is available
            try:
                clf = cv2.face.LBPHFaceRecognizer_create()
            except AttributeError:
                msgbox.showerror("Error", "OpenCV face module not available!\nPlease install opencv-contrib-python:\npip install opencv-contrib-python", parent=self.root)
                return

            # Train the classifier
            clf.train(faces, ids)
            clf.write("classifier.xml")

            unique_ids = set(ids)
            msgbox.showinfo("Result", f"Training completed successfully!\n\nDetails:\n- {len(faces)} images processed\n- {len(unique_ids)} unique person(s) trained\n- Classifier saved as 'classifier.xml'", parent=self.root)

        except Exception as e:
            msgbox.showerror("Error", f"Training failed: {str(e)}", parent=self.root)
           
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        
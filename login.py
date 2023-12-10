import face_recognition
import cv2
import sqlite3
import time
from pwinput import pwinput

def get_user_image_path(username):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT image FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def create_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    return encodings[0] if encodings else None

def verify_password(username, entered_password):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result[0] == entered_password if result else False

def login():
    username = input("Enter your username: ")
    image_path = get_user_image_path(username)

    if image_path:
        saved_face_encoding = create_face_encoding(image_path)
        video_capture = cv2.VideoCapture(0)
        start_time = time.time()

        while True:
            ret, frame = video_capture.read()
            if not ret:
                continue

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces([saved_face_encoding], face_encoding)
                if True in matches:
                    print("Success")
                    video_capture.release()
                    cv2.destroyAllWindows()
                    return True

            if time.time() - start_time > 2:
                break

        video_capture.release()
        cv2.destroyAllWindows()
        print("Face not recognized. Please enter your password.")
        password = pwinput("Enter your password: ")
        if verify_password(username, password):
            print("Login successful.")
        else:
            print("Login failed.")
    else:
        print("Username not found or image not available.")


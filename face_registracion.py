import face_recognition
import cv2

def face_id(username):


    def save_unknown_person(frame, name):
        save_path = f"/home/ashot/Desktop/Ashot/{name}.jpg"
        cv2.imwrite(save_path, frame)
        return save_path

    known_face_encodings = []
    known_face_names = []



    face_names = []
    process_this_frame = True

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame



        cv2.imshow('Video', frame)

        if "Unknown" in face_names:
            if cv2.waitKey(1) & 0xFF == ord('c'):
                image_path = save_unknown_person(frame, username)
                break

    video_capture.release()
    cv2.destroyAllWindows()
    return f'/home/ashot/Desktop/Ashot/{username}.jpg'

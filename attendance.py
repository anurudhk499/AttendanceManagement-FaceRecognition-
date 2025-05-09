import cv2
import face_recognition
import pickle
import numpy as np
import csv
from datetime import datetime

with open("face_encoding.pkl", "rb") as f:
    known_faces, known_names = pickle.load(f)

cap = cv2.VideoCapture(0)

def mark_attendance(name):
    with open("attendance.csv", "r+") as file:
        existing_data = file.readlines()
        name_list = [line.split(",")[0] for line in existing_data]
        if name not in name_list:  
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{name},{now}\n")

while True:
    _, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  
    rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        
        if True in matches:
            best_match = np.argmin(face_recognition.face_distance(known_faces, face_encoding))
            name = known_names[best_match]
            mark_attendance(name)

        y1, x2, y2, x1 = [v * 4 for v in face_location]  # Scale back to original size
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

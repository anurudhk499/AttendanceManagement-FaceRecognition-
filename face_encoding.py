import face_recognition
import os
import pickle

dataset_path = "dataset"
known_faces, known_names = [], []

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    if os.path.isdir(person_path):
        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_faces.append(encodings[0])
                known_names.append(person)

with open("face_encoding.pkl", "wb") as f:
    pickle.dump((known_faces, known_names), f)

print("✅ Face encoding completed and saved!")

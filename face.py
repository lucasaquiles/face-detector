import face_recognition

image = face_recognition.load_image_file("sachin.jpg.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
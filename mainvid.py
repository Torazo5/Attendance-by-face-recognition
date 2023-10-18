import cv2
from facerec import SimpleFacerec

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images(r"C:\Users\boosk\Downloads\images_for_face_rec")

# Load Camera
cap = cv2.VideoCapture(0)

#date checking and student listing
students = {}
with open(r'C:\Users\boosk\Downloads\students.txt') as read_file:
    for line in read_file:
        students[line.strip()] = 0 #0 is absent, 1 is present

import datetime
current_time = datetime.datetime.now()
C_time = f'{current_time.month}/{current_time.day}/{current_time.year}'


        
while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        try:
            combined = f'{name}({students[name]})'
            if (students[name] != 1):
                students[name] = 1
            
            if (students[name] == 0):
                cv2.putText(frame, combined,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            else:
                cv2.putText(frame, combined,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
        except:
            print('UNKNOWN, NOT REGISTERED')
    cv2.imshow("Frame", frame)
    with open (r'C:\Users\boosk\Downloads\attendance.txt', 'w') as file:
        file.write(f'{C_time}\n')
        for student in students:
            file.write(f'{student};{students[student]}\n')
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
# Attendance-by-face-recognition
Using face recognition to do the attendance for a class.

mainvid.py is the Python file for showing the boxes around the faces, recording the attendance, and displaying the webcam, but not the facial recognition

facerec.py is where facial recognition happens and it basically compares two images, if they are the same people, it returns True, if they aren't it returns False. This is done by encrypting each image and using the trained ai to compare the encryptions.
facerec.py compares images from images_for_facerec folder

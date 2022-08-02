import cv2
import os
import shutil

currentpath = os.getcwd()
dir = os.path.join(currentpath,"nofaces")
if not os.path.exists(dir):
    os.mkdir(dir)

os.chdir('images')
newpath = os.getcwd()
photos = os.listdir()
i = 1

face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_alt.xml')

for photo in photos:
    print(str(i)+': '+photo)
    photopath = os.path.join(newpath, photo)

    img = cv2.imread(photopath, cv2.IMREAD_UNCHANGED)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detect_faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    numface = len(detect_faces)
    if numface==0:
        # this is where the photos with no face will go to. 
        shutil.move(photopath, '../nofaces')
    
    i = i+1



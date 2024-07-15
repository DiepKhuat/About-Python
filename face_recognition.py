import cv2  # từ library opencv-pyhton
import dlib

#read the image
img = cv2.imread("anh.png")

#conver img to grayscale :3D->2D cz 3D created by color(BGR red-green-blue)
# convert 2D để execute algorithm dễ hơn (convert to grayscale)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Ensure gray is explicitly unit8
#rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#dlib: Load Face Recognition Editor
face_detector = dlib.get_frontal_face_detector()
# use detector to find face landmarks
faces = face_detector(gray)

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    cv2.rectangle(img = img, pt1=(x1,y1), pt2=(x2,y2), 
                  color=(0,255,0), thickness=3)
    break



#show the image
cv2.imshow("Face Recognition App", mat=img)
# wait for a key press to exit
cv2.waitKey(delay=0)
#Close All windows
cv2.destroyAllWindows()




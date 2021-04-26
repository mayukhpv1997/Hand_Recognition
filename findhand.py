
# Importing Libraries
import cv2

# Importing Cascades
fist_cascade = cv2.CascadeClassifier('hand.xml')
palm_cascade = cv2.CascadeClassifier('rpalm_cascade.xml')


# Making function to detect
def detect(gray, frame):
    fist = fist_cascade.detectMultiScale(gray, 1.3, 5)
    palm = palm_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in fist:
        cv2.putText(frame, 'fist', (x, y), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in palm:
        cv2.putText(frame, 'Palm', (x, y), cv2.FONT_ITALIC, 1, (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame


# Stating Camera
video_capture = cv2.VideoCapture(0)  # 0, if you have internal camera, 1 if you have externel camera

while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Also An Edge Detector in another  frame
    lower = 115
    upper = 235
    canvas = cv2.Canny(gray, lower, upper)

    cv2.imshow('Canny Edge Detector', canvas)
    detected = detect(gray, frame)
    cv2.imshow('Video', detected)

    # Press q to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()





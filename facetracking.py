import cv2
print(cv2.__version__)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)  # 0 is the default camera
while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))  # Detect faces

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)  # Display the resulting frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

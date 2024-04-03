import cv2

# Open the camera
video_capture = cv2.VideoCapture(0)

# Continuously capture video frames until the user presses 'q'
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_classifier.detectMultiScale(gray_frame, 1.1, 5, minSize=(40, 40))

    # Draw a bounding box around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

    # Display the resulting frame
    cv2.imshow("Face Detection", frame)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close the window
video_capture.release()
cv2.destroyAllWindows()
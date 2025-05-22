import cv2
import os

def stream_with_face_detection():
    """
    Streams video from the laptop's default camera and performs face detection.
    Press 'q' to quit the stream.
    """
    # 0 is usually the default camera.
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video device.")
        return

    # Load the pre-trained Haar Cascade model for face detection
    # OpenCV typically installs these XML files in its 'data' directory.
    haar_cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
    if not os.path.exists(haar_cascade_path):
        print(f"Error: Haar Cascade file not found at {haar_cascade_path}")
        print("Please ensure OpenCV is installed correctly or provide the correct path.")
        cap.release()
        return

    face_cascade = cv2.CascadeClassifier(haar_cascade_path)
    if face_cascade.empty():
        print("Error: Could not load Haar Cascade classifier.")
        cap.release()
        return

    print("Streaming video with face detection... Press 'q' to quit.")

    # --- Efficiency Parameters ---
    # Process every 'frame_skip' frames for detection
    frame_skip = 3  # Detect faces every 3rd frame
    frame_count = 0
    detected_faces = [] # Store last known faces to draw on skipped frames

    # detectMultiScale parameters (tune these for your needs)
    scale_factor = 1.1  # How much the image size is reduced at each image scale.
    min_neighbors = 5   # How many neighbors each candidate rectangle should have.
    min_face_size = (30, 30) # Minimum possible object size.

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        frame_count += 1

        # Only run detection on specified frames
        if frame_count % frame_skip == 0:
            # Convert frame to grayscale for detection (more efficient)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Perform face detection
            # detected_faces will be a list of (x, y, w, h) tuples
            detected_faces = face_cascade.detectMultiScale(
                gray_frame,
                scaleFactor=scale_factor,
                minNeighbors=min_neighbors,
                minSize=min_face_size,
                flags=cv2.CASCADE_SCALE_IMAGE
            )

        # Draw rectangles around the detected faces (using last known positions)
        for (x, y, w, h) in detected_faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # Green rectangle

        # Display the resulting frame
        cv2.imshow('Laptop Camera Stream with Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Stream ended.")

if __name__ == '__main__':
    stream_with_face_detection()
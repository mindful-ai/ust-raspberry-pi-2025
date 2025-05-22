import cv2

def stream_laptop_camera():
    """
    Streams video from the laptop's default camera.
    Press 'q' to quit the stream.
    """
    # 0 is usually the default camera. If you have multiple cameras,
    # you might need to try other indices like 1, 2, etc.
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return

    print("Streaming video... Press 'q' to quit.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('Laptop Camera Stream', frame)

        # Wait for 1 millisecond, and check if 'q' is pressed
        # 0xFF is a bitmask to get the last 8 bits of the key code
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()
    print("Stream ended.")

if __name__ == '__main__':
    stream_laptop_camera()
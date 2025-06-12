'''
wget https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
wget https://github.com/tensorflow/tensorflow/raw/master/tensorflow/lite/examples/python/label_image/mnist.tflite
'''

import cv2
import numpy as np
import tensorflow as tf

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path="mnist.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Function to preprocess ROI
def preprocess(image):
    image = cv2.resize(image, (28, 28))
    image = cv2.bitwise_not(image)
    image = image.astype(np.float32) / 255.0
    return image.reshape(1, 28, 28, 1)

# Open webcam
cap = cv2.VideoCapture(0)

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Define central ROI box
    h, w = frame.shape[:2]
    x1, y1, x2, y2 = w//2 - 100, h//2 - 100, w//2 + 100, h//2 + 100
    roi = frame[y1:y2, x1:x2]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    input_data = preprocess(thresh)

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])
    digit = np.argmax(prediction)

    # Show prediction
    cv2.putText(frame, f"Digit: {digit}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Draw box and show image
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
    cv2.imshow("Digit Recognizer", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

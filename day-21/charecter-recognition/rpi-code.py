import tflite_runtime.interpreter as tflite
import numpy as np
import cv2

# Load labels
with open("labelmap.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

# Load model
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Webcam
cap = cv2.VideoCapture(0)

def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28))
    normalized = resized.astype(np.float32) / 255.0
    return np.expand_dims(normalized, axis=(0, -1))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Extract ROI (centered box or full frame depending on setup)
    h, w, _ = frame.shape
    size = min(h, w)
    roi = frame[h//2 - size//2:h//2 + size//2, w//2 - size//2:w//2 + size//2]

    input_data = preprocess(roi)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted_class = np.argmax(output_data)
    confidence = output_data[0][predicted_class]

    label = labels[predicted_class]
    text = f"{label} ({confidence*100:.2f}%)"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Character Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

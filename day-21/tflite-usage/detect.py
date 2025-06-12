import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

# Load labels
def load_labels(path='labelmap.txt'):
    with open(path, 'r') as f:
        return {i: line.strip() for i, line in enumerate(f.readlines())}

# Load model
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

_, height, width, _ = input_details[0]['shape']
labels = load_labels()

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, (width, height))
    input_data = np.expand_dims(img, axis=0).astype(np.uint8)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    boxes = interpreter.get_tensor(output_details[0]['index'])[0]
    classes = interpreter.get_tensor(output_details[1]['index'])[0].astype(np.int32)
    scores = interpreter.get_tensor(output_details[2]['index'])[0]

    for i in range(len(scores)):
        if scores[i] > 0.5:
            ymin, xmin, ymax, xmax = boxes[i]
            (left, top, right, bottom) = (int(xmin * frame.shape[1]), int(ymin * frame.shape[0]),
                                          int(xmax * frame.shape[1]), int(ymax * frame.shape[0]))
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            label = labels.get(classes[i], "Unknown")
            cv2.putText(frame, f'{label}: {int(scores[i]*100)}%', (left, top-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('TFLite Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
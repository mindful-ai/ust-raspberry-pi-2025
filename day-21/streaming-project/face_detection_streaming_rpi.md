
# 📸 Raspberry Pi USB Webcam Face Detection & Video Streaming with Flask

This guide walks you through implementing real-time **face detection** using a USB webcam and **streaming it** via a Flask web server on a Raspberry Pi.

---

## ✅ Requirements

- Raspberry Pi (Bookworm OS or similar)
- USB Webcam
- Python 3
- OpenCV
- Flask

---

## 🧰 1. Install Required Packages

```bash
sudo apt update
sudo apt install python3-opencv python3-flask python3-pip
```

Verify OpenCV installation:

```bash
python3 -c "import cv2; print(cv2.__version__)"
```

---

## 📁 2. Setup Project Directory

```bash
mkdir ~/face-streaming
cd ~/face-streaming
```

Download Haarcascade file:

```bash
wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml
```

---

## 🧠 3. Create `app.py`

Create a file called `app.py` with the following content:

```python
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)  # 0 is the USB webcam

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return '''
    <html>
        <head><title>Face Detection Stream</title></head>
        <body>
            <h1>Face Detection Live Stream</h1>
            <img src="/video_feed">
        </body>
    </html>
    '''

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

---

## 🚀 4. Run the Server

```bash
python3 app.py
```

Open a browser on another device on the same network:

```
http://<raspberrypi_IP>:5000
```

Find the IP:

```bash
hostname -I
```

---

## 🔁 5. Optional: Run on Boot

Add this line to your crontab:

```bash
crontab -e
```

```bash
@reboot /usr/bin/python3 /home/pi/face-streaming/app.py &
```

---

## 🧪 Test Checklist

| Test                        | Expected Result                  |
|----------------------------|----------------------------------|
| Visit Flask page           | Live video stream                |
| Move face in webcam view   | Blue rectangle drawn on face     |

---

## 🧼 Troubleshooting

| Problem              | Solution                          |
|----------------------|-----------------------------------|
| No video             | Check `ls /dev/video0`            |
| Flask not accessible | Check firewall, correct IP        |
| Laggy video          | Lower resolution or frame rate    |

---

Happy coding! 🎥

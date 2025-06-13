# 🚘 Smart License Plate Detection & Logging System  
### *A Full-Stack IoT System with OCR, OpenCV, Flask, Tkinter, MQTT, SQLite, Logging, and ThingsBoard Integration*

---

## 🎯 Objective

Design and develop a full-stack IoT system using Raspberry Pi that:

- Detects and reads vehicle license plates using a webcam and OCR.
- Logs detections locally using SQLite and structured logging.
- Provides:
  - A **Tkinter-based local dashboard** on the Pi.
  - A **Flask-based remote admin panel** for system control and log access.
  - Real-time **MQTT streaming** of detection events.
  - A **centralized ThingsBoard cloud dashboard** to monitor and visualize plate logs.
- Supports **CI/CD** workflows via GitHub Actions.

Students will integrate image processing, IoT communication, database handling, UI/UX, cloud integration, and DevOps practices in a single deployable project.

---

## 🧰 Hardware Requirements

| Component            | Description |
|----------------------|-------------|
| Raspberry Pi 4/5     | Core processing unit |
| Pioneer600 HAT       | Optional GPIO interface for alarms/LEDs |
| USB Webcam / Pi Camera | Video capture |
| Laptop               | For admin access and testing |
| Internet Access      | Required for MQTT and ThingsBoard |

---

## ⚙️ Software Stack

### 🐍 Python Libraries
- `opencv-python`
- `easyocr` or `pytesseract`
- `tkinter`
- `flask`
- `sqlite3`
- `paho-mqtt`
- `logging`
- `threading`, `datetime`, `os`, `re`, `json`

### 🌐 Cloud Dashboard
- **ThingsBoard Cloud** – Device telemetry visualization

### 🛠 DevOps & CI/CD
- GitHub + GitHub Actions
- Optionally: Docker for Flask

---

## 🧠 Functional Components

### 1. 🎥 Real-Time Detection
- Webcam capture via OpenCV.
- Plate region extraction + OCR (EasyOCR or pytesseract).
- Pre-processing pipeline for better recognition.

### 2. 📝 SQLite + Logging
- Store logs with plate, time, confidence, snapshot path.
- Local SQLite DB `plate_logs`.
- Use rotating `detection.log` for debug/info/error logs.

### 3. 🖥 Tkinter Dashboard
- Live feed display.
- Last detected plate.
- Status and last 10 entries.

### 4. 🌐 Flask Admin Panel
- `/logs`, `/settings`, `/export`, `/start`, `/stop`.
- View logs, adjust settings, download CSV, control engine.
- Optional password auth.

### 5. 📡 MQTT Integration
- Topic: `pi/license_plate`
- Publishes plate ID, timestamp, confidence.
- Option to use local or remote broker.

### 6. 📊 ThingsBoard Cloud Dashboard
- Register Pi as a device.
- Push telemetry via MQTT or REST.
- Visualize:
  - Live plate stream
  - Plates per day/hour
  - Tabular logs
  - Map view (static/mock GPS)

### 7. 🔁 CI/CD
- GitHub Actions workflow.
- Auto-deploy to Pi via SSH.
- Run tests, install dependencies, restart service.

---

## 📁 Project Structure

```
smart-license-plate/
├── main.py
├── ocr_utils.py
├── db_utils.py
├── log_utils.py
├── mqtt_client.py
├── camera_utils.py
├── tkinter_dashboard.py
├── flask_admin/
│   ├── app.py
│   └── templates/
├── logs/
│   ├── detection.log
│   └── plates.db
├── thingsboard/
│   ├── tb_client.py
│   └── device-config.json
├── .github/
│   └── workflows/
│       └── deploy.yml
├── requirements.txt
└── README.md
```

---

## ⏱ Suggested Time Breakdown (16 hrs)

| Time | Task |
|------|------|
| 1 hr | Raspberry Pi + webcam setup |
| 2 hrs | OpenCV-based plate detection |
| 2 hrs | OCR integration and result parsing |
| 1 hr | SQLite DB logging + structured logs |
| 2 hrs | Tkinter dashboard development |
| 2 hrs | Flask admin with settings and DB viewer |
| 1 hr | MQTT setup and testing |
| 2 hrs | ThingsBoard dashboard + data publishing |
| 2 hrs | CI/CD with GitHub Actions |
| 1 hr | Testing, polish, and documentation |

---

## 📊 Evaluation Rubric (100 points)

| Criteria                             | Points |
|-------------------------------------|--------|
| Plate detection + OCR accuracy      | 15     |
| SQLite logging + error logs         | 10     |
| Local Tkinter dashboard             | 10     |
| Flask admin panel (settings/logs)   | 15     |
| MQTT communication                  | 10     |
| ThingsBoard cloud dashboard         | 15     |
| CI/CD pipeline via GitHub Actions   | 10     |
| Code quality, modularity, comments  | 5      |
| Final demo and presentation         | 10     |

---

## ✅ Final Deliverables

1. Functional Raspberry Pi system
2. Tkinter dashboard
3. Flask admin panel
4. Working MQTT & ThingsBoard link
5. GitHub repo with documentation

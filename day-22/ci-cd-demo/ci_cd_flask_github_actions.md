
# 🚀 CI/CD with Flask, Pytest, GitHub Actions & Raspberry Pi Deployment

## 🎯 Objective

Demonstrate Full CI/CD Flow using:
- Flask web app
- Pytest for testing
- GitHub Actions for CI
- Raspberry Pi as the deployment server (CD)

---

## 🧱 Folder Structure

```
flask-ci-cd-demo/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── app.py
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
```

---

# 🔵 STEP 1: Setup Flask with ONE Endpoint and Deploy

## ✅ 1.1 Code the App

**app/main.py**
```python
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return jsonify(message="Hello from Flask CI/CD")

    return app
```

**app.py**
```python
from app.main import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**requirements.txt**
```
Flask
pytest
```

## ✅ 1.2 Add Tests

**tests/test_main.py**
```python
from app.main import create_app

def test_index():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from Flask CI/CD"}
```

## ✅ 1.3 Initialize Git and Push to GitHub

```bash
git init
git add .
git commit -m "Step 1: Initial endpoint and test"
git branch -M main
git remote add origin https://github.com/<your-username>/flask-ci-cd-demo.git
git push -u origin main
```

## ✅ 1.4 Setup GitHub Actions (CI)

**.github/workflows/ci.yml**
```yaml
name: CI-CD Workflow

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest
```

## ✅ 1.5 Setup Raspberry Pi (CD Target)

```bash
sudo apt update
sudo apt install python3-venv git -y

git clone https://github.com/<your-username>/flask-ci-cd-demo.git
cd flask-ci-cd-demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

---

# 🔴 STEP 2: Add NEW Endpoint + Test → Redeploy

## ✅ 2.1 Add New Endpoint `/status`

**Add to app/main.py**
```python
@app.route("/status")
def status():
    return jsonify(status="OK", environment="raspberry-pi")
```

## ✅ 2.2 Add Test

**tests/test_main.py**
```python
def test_status():
    app = create_app()
    client = app.test_client()
    response = client.get("/status")
    assert response.status_code == 200
    assert response.get_json() == {"status": "OK", "environment": "raspberry-pi"}
```

## ✅ 2.3 Push Changes

```bash
git checkout -b feature/status-endpoint
git add .
git commit -m "Step 2: Added /status endpoint and test"
git push -u origin feature/status-endpoint
```

## ✅ 2.4 Create Pull Request

- Go to GitHub repository
- Click “Compare & pull request”
- Submit PR

## ✅ 2.5 Merge & Redeploy

```bash
cd flask-ci-cd-demo
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
pkill -f app.py
nohup python app.py &
```

---

# 📘 Explanation of ci.yml

| Section | Purpose |
|--------|---------|
| `on` | Trigger CI on push/PR to main |
| `jobs.test.runs-on` | Use Ubuntu runner |
| `checkout` | Load repo code |
| `setup-python` | Set Python 3.10 |
| `pip install` | Install deps |
| `pytest` | Run tests |

---

# 🧑‍🏫 Additional Information

## 🎓 Goals

- Understand Pull Requests
- See what happens when CI fails and passes
- Experience fixing a test failure in PR

## 🚧 Broken PR Demo

1. Create branch:
```bash
git checkout -b feature/status-endpoint
```

2. Break the `/status` endpoint:
```python
@app.route("/status")
def status():
    return jsonify(status="BAD", environment="raspberry-pi")
```

3. Add test expecting correct value

4. Push & Open PR

5. Watch CI fail

6. Fix endpoint to match test, push again

7. Watch CI pass and merge

## ✅ Deploy

On Pi:
```bash
git pull origin main
pkill -f app.py
nohup python app.py &
```

---

## 📈 Teaching Tips

| Action | Purpose |
|--------|--------|
| Break test | Show CI gates failing code |
| Fix and push | Auto re-trigger CI |
| Merge only after green | Teach discipline |
| Deploy manually | Show end-to-end loop |

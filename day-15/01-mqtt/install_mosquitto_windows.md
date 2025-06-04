
# Installing MQTT Broker (Mosquitto) on Windows

## 🛠️ Step-by-Step: Installing Mosquitto Broker on Windows

### ✅ Step 1: Download Mosquitto
1. Visit the official Mosquitto downloads page:  
   👉 https://mosquitto.org/download/
2. Under **Windows**, download the appropriate installer (e.g., `mosquitto-2.0.xx-install-windows-x64.exe`).

### ✅ Step 2: Run the Installer
1. Launch the installer (`.exe` file).
2. During installation:
   - Select **“Install service”** if you want Mosquitto to start automatically.
   - Choose the default configuration unless you need customization.

### ✅ Step 3: Install Dependencies
- The installer typically includes dependencies, but if needed:
  - Install **OpenSSL** for encrypted communication:  
    👉 https://slproweb.com/products/Win32OpenSSL.html
  - Install **Visual C++ Redistributable** if prompted:  
    👉 https://aka.ms/vs/17/release/vc_redist.x64.exe

### ✅ Step 4: Add Mosquitto to System Path (Optional but Useful)
1. Add the Mosquitto installation folder to your Windows **PATH** environment variable to run `mosquitto` from any terminal.

### ✅ Step 5: Start Mosquitto Broker
1. Open **Command Prompt** or **PowerShell**.
2. Run:
   ```sh
   mosquitto
   ```
   - This starts the broker with the default config (usually on port `1883`).
   - You can also use a custom config:
     ```sh
     mosquitto -c mosquitto.conf
     ```

## 🔍 Test the Installation

### Open two terminals:

- **Terminal 1 (Subscriber)**:
  ```sh
  mosquitto_sub -t test/topic -h localhost
  ```

- **Terminal 2 (Publisher)**:
  ```sh
  mosquitto_pub -t test/topic -m "Hello from Windows" -h localhost
  ```

You should see the message appear in Terminal 1.

## 🧰 Logs and Config
- **Default config location**: `C:\Program Files\mosquitto\mosquitto.conf`
- You can customize:
  - Logging
  - Authentication
  - TLS/SSL
  - Persistence

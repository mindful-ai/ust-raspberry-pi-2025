✅ STEP 1: Save Your Application
Ensure your script (kiosk.py) is saved in a permanent location, e.g.:
/home/pi/payment_kiosk/kiosk.py

Make sure it works by running:
python3 /home/pi/payment_kiosk/kiosk.py

✅ STEP 2: Make It Executable (Optional but Good Practice)
chmod +x /home/pi/payment_kiosk/kiosk.py


✅ STEP 3: Create a Desktop Autostart File
Create a directory if it doesn’t exist:
mkdir -p /home/pi/.config/autostart

Create an autostart entry:
nano /home/pi/.config/autostart/kiosk.desktop

Paste the following content:
[Desktop Entry]
Type=Application
Name=Payment Kiosk
Exec=python3 /home/pi/payment_kiosk/kiosk.py
StartupNotify=false
Terminal=false

Save and exit (Ctrl+O, Enter, then Ctrl+X)

✅ STEP 4: Test It
Reboot your Raspberry Pi:
sudo reboot

After rebooting, the Tkinter GUI should start automatically on the desktop.
# Raspberry Pi Kiosk Mode Setup for Tkinter Payment App

This guide helps you set up a full **Kiosk Mode** on a Raspberry Pi (Bookworm OS) to launch a Tkinter GUI payment application on boot in fullscreen, blocking access to the desktop.

---

## ✅ 1. Enable Auto-Login to Desktop

1. Open configuration tool:

    ```bash
    sudo raspi-config
    ```

2. Navigate to:

    ```
    1 System Options → S5 Boot / Auto Login → B2 Console Autologin with Desktop
    ```

3. Select: **Desktop Autologin**

4. Reboot:

    ```bash
    sudo reboot
    ```

---

## ✅ 2. Modify Your Tkinter Script for Fullscreen

Edit your `kiosk.py`:

```python
self.root = tk.Tk()
self.root.attributes("-fullscreen", True)  # Fullscreen mode

# Optional: Allow exiting with ESC (remove in production)
self.root.bind("<Escape>", lambda e: self.root.destroy())


## ✅ 3. Create Autostart File

Create the autostart directory if it doesn’t exist:

mkdir -p /home/pi/.config/autostart

Create and edit autostart file:

nano /home/pi/.config/autostart/kiosk.desktop

Add this content:

[Desktop Entry]
Type=Application
Name=Payment Kiosk
Exec=python3 /home/pi/payment_kiosk/kiosk.py
StartupNotify=false
Terminal=false

Make sure kiosk.py is located exactly at that path.

## ✅ 4. (Optional) Hide Mouse Cursor
Install unclutter to hide the mouse after inactivity:


sudo apt install unclutter
Then it will automatically hide the cursor after a few seconds of no movement.

✅ 5. (Optional) Disable Screen Blanking / Power Saving
To prevent screen from turning off:


sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
Add these lines at the end:


@xset s off
@xset -dpms
@xset s noblank

## ✅ 6. Reboot and Test

sudo reboot


Your Pi should now:

    Auto-login to desktop
    Launch your Tkinter app in fullscreen
    Not show the desktop or taskbar

💡 Optional Hardening for Deployment

    Physically cover USB ports / keyboard input
    Use a minimal window manager like matchbox for ultra-locked-down mode
    Set up remote SSH for maintenance access
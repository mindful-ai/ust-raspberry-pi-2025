
# 📶 Raspberry Pi Bookworm OS - Wi-Fi Configuration Scenarios

This guide outlines several useful scenarios for configuring Wi-Fi on a Raspberry Pi running Raspberry Pi OS Bookworm, which uses **NetworkManager** by default.

---

## 📌 Scenario 1: Add Wi-Fi SSID and Password using `nmcli` (Recommended)

```
nmcli dev wifi connect "YOUR_SSID" password "YOUR_PASSWORD"
```

- Saves the network for future reboots.
- Auto-connects when in range.

---

## 📌 Scenario 2: Add Wi-Fi Manually using `nmcli`

```
nmcli connection add type wifi ifname wlan0 con-name homewifi ssid "YOUR_SSID"
nmcli connection modify homewifi wifi-sec.key-mgmt wpa-psk
nmcli connection modify homewifi wifi-sec.psk "YOUR_PASSWORD"
nmcli connection up homewifi
```

- Useful if you want to predefine a profile.

---

## 📌 Scenario 3: Use `wpa_supplicant.conf` (Legacy, Not Recommended on Bookworm)

Only use this if NetworkManager is **disabled**.

### File: `/etc/wpa_supplicant/wpa_supplicant.conf`

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IN

network={
    ssid="YOUR_SSID"
    psk="YOUR_PASSWORD"
    key_mgmt=WPA-PSK
}
```

### Enable wpa_supplicant (if using this method):

```
sudo systemctl stop NetworkManager
sudo systemctl enable wpa_supplicant
sudo systemctl start wpa_supplicant
```

---

## 📌 Scenario 4: Mark Interface as Unmanaged by NetworkManager

To use `wpa_supplicant` on `wlan0`:

### Edit `/etc/NetworkManager/NetworkManager.conf`:

```
[keyfile]
unmanaged-devices=interface-name:wlan0
```

Then restart:

```
sudo systemctl restart NetworkManager
```

---

## 📌 Scenario 5: Set Static IP Using `nmcli`

```
nmcli con modify "YOUR_SSID" ipv4.addresses 192.168.1.50/24
nmcli con modify "YOUR_SSID" ipv4.gateway 192.168.1.1
nmcli con modify "YOUR_SSID" ipv4.dns 8.8.8.8
nmcli con modify "YOUR_SSID" ipv4.method manual
nmcli con up "YOUR_SSID"
```

---

## 📌 Scenario 6: Autoconnect on Boot

```
nmcli con modify "YOUR_SSID" connection.autoconnect yes
```

---

## 📌 Scenario 7: Forget or Delete a Network

```
nmcli connection delete "YOUR_SSID"
```

---

## ✅ Recommended Practice for Bookworm

- Always use **`nmcli`** for managing networks.
- Avoid modifying `wpa_supplicant.conf` unless you're in a minimal headless setup and explicitly disabling NetworkManager.

---

© 2025 Raspberry Pi Wi-Fi Setup Guide

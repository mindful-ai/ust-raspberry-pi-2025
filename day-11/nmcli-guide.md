
# 📘 Understanding `nmcli` (Network Manager Command Line Interface)

`nmcli` is a command-line tool for managing **NetworkManager** in Linux. It allows you to create, display, edit, delete, activate, and deactivate network connections, as well as control the network interfaces.

---

## 🧠 Why Use `nmcli`?

- Manage Wi-Fi, Ethernet, and mobile connections without a GUI
- Automate network configuration in scripts
- Useful for headless systems like Raspberry Pi

---

## 🛠 Common `nmcli` Commands

### 🔍 Check Device and Connection Status

```bash
nmcli device status
```

Lists all network devices and their current states.

---

### 📡 List Available Wi-Fi Networks

```bash
nmcli device wifi list
```

Scans and lists available wireless networks.

---

### 🔌 Connect to a Wi-Fi Network

```bash
nmcli device wifi connect <SSID> password <PASSWORD>
```

Example:
```bash
nmcli device wifi connect HomeWiFi password mysecret123
```

---

### 🔗 Show Active Connections

```bash
nmcli connection show --active
```

Shows connections currently in use.

---

### 🔌 Disconnect a Network

```bash
nmcli device disconnect wlan0
```

Replace `wlan0` with your Wi-Fi interface name.

---

### 🔄 Reconnect a Device

```bash
nmcli device connect wlan0
```

---

### 🧾 Add a New Connection (Manual IP)

```bash
nmcli connection add type ethernet con-name static-ip ifname eth0 ip4 192.168.1.100/24 gw4 192.168.1.1
```

Adds a static IP configuration for the Ethernet interface.

---

### 🧼 Delete a Connection

```bash
nmcli connection delete <connection_name>
```

List them with:
```bash
nmcli connection show
```

---

## 🧪 Examples

### Example 1: Set a Static IP for Wi-Fi

```bash
nmcli con mod "HomeWiFi" ipv4.method manual ipv4.addresses 192.168.1.150/24 ipv4.gateway 192.168.1.1 ipv4.dns "8.8.8.8 1.1.1.1"
nmcli con up "HomeWiFi"
```

---

### Example 2: Automatically Connect on Boot

```bash
nmcli connection modify HomeWiFi connection.autoconnect yes
```

---

## 🧯 Troubleshooting

- **No device found?** Check if NetworkManager is running:
  ```bash
  systemctl status NetworkManager
  ```
- **Interface down?**
  ```bash
  nmcli device set wlan0 managed yes
  nmcli device connect wlan0
  ```

---

## ✅ Summary

| Task                          | Command Example                                      |
|-------------------------------|------------------------------------------------------|
| List devices                  | `nmcli device status`                                |
| List Wi-Fi networks           | `nmcli device wifi list`                             |
| Connect to Wi-Fi              | `nmcli device wifi connect SSID password PASSWORD`   |
| Disconnect device             | `nmcli device disconnect wlan0`                      |
| Show active connections       | `nmcli connection show --active`                     |
| Modify static IP              | `nmcli con mod "HomeWiFi" ipv4.method manual ...`    |

---

© 2025 `nmcli` Reference Guide

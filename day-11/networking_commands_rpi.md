# Networking Commands for Raspberry Pi

This guide provides essential and frequently used networking commands for Raspberry Pi, categorized by purpose. These commands help manage Wi-Fi, troubleshoot issues, monitor network status, and configure IP settings.

---

## 🛰️ Wi-Fi Management

### Q: What are the available Wi-Fi networks?
**A:**
```bash
nmcli device wifi list
```

### Q: How to scan Wi-Fi networks using `iwlist`?
**A:**
```bash
sudo iwlist wlan0 scan | grep ESSID
```

### Q: How to connect to a Wi-Fi network using `nmcli`?
**A:**
```bash
nmcli dev wifi connect "SSID_NAME" password "WIFI_PASSWORD"
```

### Q: How to connect to a hidden Wi-Fi network?
**A:**
```bash
nmcli dev wifi connect "SSID_NAME" password "PASSWORD" hidden yes
```

### Q: How to disconnect from a Wi-Fi network?
**A:**
```bash
nmcli con down id "SSID_NAME"
```

### Q: How to reconnect to a known Wi-Fi network?
**A:**
```bash
nmcli con up id "SSID_NAME"
```

### Q: How to configure Wi-Fi manually using `wpa_supplicant`?
**A:**
Edit:
```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
Add:
```conf
network={
    ssid="Your_SSID"
    psk="Your_PASSWORD"
}
```
Apply:
```bash
sudo wpa_cli -i wlan0 reconfigure
```

### Q: How to enable/disable Wi-Fi?
**A:**
```bash
nmcli radio wifi off
nmcli radio wifi on
```
or
```bash
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
```

---

## 🌐 Network Configuration

### Q: What is my IP address?
**A:**
```bash
hostname -I
```

### Q: How to view detailed network interface information?
**A:**
```bash
ifconfig
```

### Q: How to display the MAC address of interfaces?
**A:**
```bash
ip link show
```

### Q: How to set a static IP address?
**A:**
Edit:
```bash
sudo nano /etc/dhcpcd.conf
```
Add:
```conf
interface wlan0
static ip_address=192.168.1.50/24
static routers=192.168.1.1
static domain_name_servers=8.8.8.8
```

### Q: How to check current routing table?
**A:**
```bash
route -n
```

### Q: How to check default gateway?
**A:**
```bash
ip route | grep default
```

---

## 🔍 Troubleshooting & Diagnostics

### Q: How to ping a website?
**A:**
```bash
ping -c 4 google.com
```

### Q: How to trace the route to a remote host?
**A:**
```bash
traceroute google.com
```

### Q: How to test DNS resolution?
**A:**
```bash
nslookup openai.com
```
or
```bash
dig openai.com
```

### Q: How to restart networking services?
**A:**
```bash
sudo systemctl restart networking
```
or
```bash
sudo systemctl restart dhcpcd
```

### Q: How to release and renew DHCP IP?
**A:**
```bash
sudo dhclient -r
sudo dhclient
```

### Q: How to flush DNS cache?
**A:**
```bash
sudo systemd-resolve --flush-caches
```

### Q: How to check DNS servers in use?
**A:**
```bash
cat /etc/resolv.conf
```

---

## 📈 Monitoring & Security

### Q: How to check all open ports?
**A:**
```bash
sudo netstat -tuln
```

### Q: How to scan for nearby devices?
**A:**
```bash
sudo nmap -sn 192.168.1.0/24
```

### Q: How to check if a specific port is open on a host?
**A:**
```bash
nc -zv 192.168.1.1 22
```

### Q: How to find public IP address?
**A:**
```bash
curl ifconfig.me
```

### Q: How to show active sockets and connections?
**A:**
```bash
ss -tunapl
```

---

## 🧰 Miscellaneous

### Q: How to unblock Wi-Fi using `rfkill`?
**A:**
```bash
sudo rfkill unblock wifi
```

### Q: How to check the status of all connections?
**A:**
```bash
nmcli connection show
```

### Q: How to view wireless interface and signal strength?
**A:**
```bash
iwconfig
```

---

> 💡 **Tip:** Always use `sudo` for commands that change system settings or require root access.
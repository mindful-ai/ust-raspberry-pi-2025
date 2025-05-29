# 📡 Raspberry Pi Networking Commands (Wired & Wi-Fi)

A comprehensive reference of commonly used networking commands for Raspberry Pi, categorized and written in Q&A format for clarity and practical use.

---

## 🛰️ Wi-Fi Management

### Q: What are the available Wi-Fi networks?
**A:**
```bash
nmcli device wifi list
```

### Q: How to connect to a Wi-Fi network using `nmcli`?
**A:**
```bash
nmcli device wifi connect "SSID" password "PASSWORD"
```

### Q: How to list saved Wi-Fi connections?
**A:**
```bash
nmcli connection show
```

### Q: How to delete a saved Wi-Fi connection?
**A:**
```bash
nmcli connection delete "SSID"
```

### Q: How to reconnect to a known Wi-Fi?
**A:**
```bash
nmcli connection up id "SSID"
```

### Q: How to disconnect from the current Wi-Fi?
**A:**
```bash
nmcli connection down id "SSID"
```

### Q: How to scan for Wi-Fi networks using `iwlist`?
**A:**
```bash
sudo iwlist wlan0 scan | grep ESSID
```

### Q: How to view Wi-Fi signal strength?
**A:**
```bash
iwconfig wlan0
```

### Q: How to bring Wi-Fi interface up or down?
**A:**
```bash
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
```

### Q: How to block/unblock Wi-Fi using `rfkill`?
**A:**
```bash
rfkill block wifi
rfkill unblock wifi
```

---

## 🌐 Wired Network Configuration

### Q: How to check current IP address?
**A:**
```bash
hostname -I
```

### Q: How to view all network interfaces?
**A:**
```bash
ip addr show
```

### Q: How to check network interface status?
**A:**
```bash
nmcli device status
```

### Q: How to restart network manager?
**A:**
```bash
sudo systemctl restart NetworkManager
```

### Q: How to assign a static IP address?
**A:**
Edit `/etc/dhcpcd.conf` and add:
```conf
interface eth0
static ip_address=192.168.1.100/24
static routers=192.168.1.1
static domain_name_servers=8.8.8.8
```

---

## 🔍 Troubleshooting & Diagnostics

### Q: How to ping a website?
**A:**
```bash
ping -c 4 google.com
```

### Q: How to check if a host is reachable?
**A:**
```bash
ping 8.8.8.8
```

### Q: How to test DNS resolution?
**A:**
```bash
nslookup openai.com
```

### Q: How to get routing table?
**A:**
```bash
route -n
```

### Q: How to trace a route to a host?
**A:**
```bash
traceroute google.com
```

### Q: How to check default gateway?
**A:**
```bash
ip route | grep default
```

### Q: How to flush DNS cache?
**A:**
```bash
sudo systemd-resolve --flush-caches
```

### Q: How to check current DNS settings?
**A:**
```bash
cat /etc/resolv.conf
```

---

## 📊 Monitoring & Inspection

### Q: How to check all active network connections?
**A:**
```bash
netstat -tulnp
```

### Q: How to find open ports?
**A:**
```bash
sudo lsof -i -P -n
```

### Q: How to monitor network usage?
**A:**
```bash
iftop -i wlan0
```

### Q: How to display all connected devices on LAN?
**A:**
```bash
sudo nmap -sn 192.168.1.0/24
```

### Q: How to test port connectivity?
**A:**
```bash
nc -zv 192.168.1.1 22
```

---

## 🛠️ Interface & Services

### Q: How to enable/disable networking completely?
**A:**
```bash
nmcli networking off
nmcli networking on
```

### Q: How to restart DHCP client?
**A:**
```bash
sudo dhclient -r
sudo dhclient
```

### Q: How to get MAC address of an interface?
**A:**
```bash
cat /sys/class/net/wlan0/address
```

### Q: How to check link speed?
**A:**
```bash
ethtool eth0 | grep Speed
```

### Q: How to enable IPv4 forwarding?
**A:**
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

### Q: How to stop a service running on a port? 
**A:**
```bash
sudo lsof -i :8080
sudo systemctl stop <service_name>
```

##### or Forcibly kill the process as last resort
The fuser command in Linux is used to identify which processes are using a file, directory, or socket (like a network port). It’s especially useful for managing files or ports that are being held open by running processes.

```bash
sudo fuser -k 8080/tcp
```
---

## 🌐 Miscellaneous

### Q: How to get external IP address?
**A:**
```bash
curl ifconfig.me
```

### Q: How to show current connection details?
**A:**
```bash
nmcli device show wlan0
```

### Q: How to disable IPv6?
**A:**
Edit `/etc/sysctl.conf` and add:
```conf
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
```

---

> ⚠️ **Note**: Some commands may require installation (e.g., `nmap`, `iftop`, `ethtool`) using `sudo apt install <tool>`.
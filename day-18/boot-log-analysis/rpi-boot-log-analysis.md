
# Accessing and Analyzing the Boot Log of a Raspberry Pi

Accessing and analyzing the **boot log** of a **Raspberry Pi** can help diagnose issues with hardware, services, or startup sequences. Here's how to do it step by step.

---

## ✅ 1. Accessing the Raspberry Pi

Connect to your Raspberry Pi via:
- Monitor + keyboard directly, or
- SSH:
  ```bash
  ssh pi@<raspberry-pi-ip>
  ```

---

## ✅ 2. Viewing Boot Logs

### 🔹 a. `dmesg` – Kernel ring buffer (recent boot events)
```bash
dmesg | less
```
- Shows kernel-level messages.
- Useful for hardware detection, driver issues, etc.

🔍 To look for errors:
```bash
dmesg --color=always | grep -iE 'error|fail|warn'
```

---

### 🔹 b. `journalctl` – Systemd journal logs

**Entire boot log:**
```bash
sudo journalctl -b
```

**Previous boot:**
```bash
sudo journalctl -b -1
```

**Filter by service:**
```bash
sudo journalctl -u <service-name>
```

**Only errors:**
```bash
sudo journalctl -p err -b
```

⏱️ Add `--since` or `--until` for time-based filters:
```bash
sudo journalctl --since "10 minutes ago"
```

---

### 🔹 c. `/var/log/boot.log` – Boot services log
```bash
cat /var/log/boot.log
```
> ⚠️ This file may not be available in newer Raspberry Pi OS versions using systemd unless `bootlogd` is manually enabled.

---

## ✅ 3. Enabling Persistent Logs (optional)

If `journalctl` doesn't show full history after reboot, enable persistent logging:
```bash
sudo mkdir -p /var/log/journal
sudo systemctl restart systemd-journald
```

---

## ✅ 4. Analyzing the Boot Log

### 🔎 Common things to look for:
- ❗ `Failed` or `Error` messages
- 🕓 Services taking a long time to start
- 🔌 Hardware/driver issues (e.g., USB devices not detected)
- ❌ Filesystem mount failures
- ⚠️ Warnings from third-party applications or custom scripts

### Example filter:
```bash
sudo journalctl -b | grep -i 'fail'
```

### Save log to file for deep analysis:
```bash
sudo journalctl -b > bootlog.txt
```

Then analyze using:
- `less bootlog.txt`
- or open it on a PC using a text editor or `grep`.

---

## ✅ 5. Bonus: Timing Analysis

Use `systemd-analyze` to see boot time:
```bash
systemd-analyze
```

Breakdown of services:
```bash
systemd-analyze blame
```

Graphical output (SVG):
```bash
systemd-analyze plot > boot.svg
```
> Open the `boot.svg` file on a PC to visualize startup delays.

---

## 🔚 Summary

| Command | Purpose |
|--------|---------|
| `dmesg` | Kernel boot messages |
| `journalctl -b` | Full system log of current boot |
| `journalctl -b -1` | Previous boot log |
| `systemd-analyze` | Boot time statistics |
| `/var/log/boot.log` | Traditional boot log (if enabled) |

To connect and use storage devices (like USB flash drives, SSDs, or HDDs) on a Raspberry Pi, you can follow these steps. This guide covers USB-based storage devices and assumes you're using a Raspberry Pi OS (Bookworm/Bullseye/Buster) setup.

🧰 What You'll Need

Raspberry Pi (any model with USB ports)

USB flash drive or external SSD/HDD

Power supply (ensure it’s sufficient—especially for SSDs)

Keyboard, mouse, display or SSH access

🛠 Step-by-Step: Mounting a USB Storage Device

🔌 1. Plug in the USB Device

Insert the USB stick or connect the external SSD to one of the Pi’s USB ports. You should hear a click or see a status LED on the drive.

🔍 2. Check the Device Recognition


lsblk
or
sudo fdisk -l

You’ll see something like:


sda      8:0    1  14.9G  0 disk
└─sda1   8:1    1  14.9G  0 part
This means your USB device is /dev/sda1.

📂 3. Create a Mount Point

sudo mkdir /mnt/myusb
You can name myusb anything you like.

🔧 4. Mount the USB Drive

sudo mount /dev/sda1 /mnt/myusb
Now the USB storage is accessible at /mnt/myusb.

📑 5. Verify Access
List files to confirm:

ls /mnt/myusb
You should see the contents of your USB device.

🔒 6. Unmount When Done
Before unplugging:

sudo umount /mnt/myusb
📝 Automount on Boot (Optional)
To mount the drive automatically on boot:

1. Get UUID of the device:

sudo blkid
Example output:


/dev/sda1: UUID="A1B2-C3D4" TYPE="vfat"

2. Edit /etc/fstab:

sudo nano /etc/fstab
Add a line:


UUID=A1B2-C3D4 /mnt/myusb vfat defaults,nofail 0 0

Replace vfat with ext4, ntfs, or exfat as needed depending on the filesystem.

⚠️ Notes for SSDs/HDDs

Power Requirements: Use a powered USB hub if your drive needs more power than the Pi can supply.

exFAT Support:


sudo apt install exfat-fuse exfat-utils
NTFS Support:


sudo apt install ntfs-3g

💡 Example: Automounting an External SSD

Let’s say you have an SSD with ext4 filesystem, and its UUID is 1234-5678.

Steps:

Create mount point:


sudo mkdir /mnt/ssd
Add to /etc/fstab:


UUID=1234-5678 /mnt/ssd ext4 defaults,nofail 0 0
Test:


sudo mount -a


Let’s assume your storage device is mounted at /mnt/myusb.

✅ Python Code Example: Read/Write a File

```python
# File path on the mounted USB device
file_path = "/mnt/myusb/sample.txt"

# Writing to the file
with open(file_path, "w") as file:
    file.write("Hello from Raspberry Pi!\n")
    file.write("This file is stored on a USB drive.\n")

# Reading from the file
with open(file_path, "r") as file:
    contents = file.read()
    print("File contents:")
    print(contents)
```

🧪 Output (Terminal)

Hello from Raspberry Pi!
This file is stored on a USB drive.

⚠️ Ensure:

The USB device is mounted (e.g., /mnt/myusb exists).

You have write permissions. If not, use sudo chown pi:pi /mnt/myusb to give access to the pi user.

The path in your Python code matches the actual mount path.

Would you like a .py version or a project example that logs sensor data to USB?









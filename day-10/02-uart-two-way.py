import serial
import time

# Replace 'COM3' with the correct COM port from Device Manager
ser = serial.Serial('COM3', 9600)

try:
    while True:
        # Send a message
        msg = "Hello from Windows!"
        ser.write((msg + "\n").encode('utf-8'))
        print(f"Sent: {msg}")

        # Try to read a message
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Received: {line}")

        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()

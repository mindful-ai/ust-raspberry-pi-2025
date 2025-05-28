import serial
import time

ser = serial.Serial("/dev/ttyAMA0", 9600)

try:
	while True:
		msg =  "Hi from Pi!"
		ser.write((msg+"\n").encode('utf-8'))
		print(f"Sent: {msg}")

		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').strip()
			if line:
				print(f"Received: {line}")
		time.sleep(2)

except KeyboardInterrupt:
	print("Exiting...")
finally:
	ser.close()

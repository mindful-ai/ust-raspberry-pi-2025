import serial

ser = serial.Serial("/dev/ttyAMA0", 9600)

ser.write("Hello World!".encode())
try:
	while True:
		print(ser.read().decode())
		ser.write("Hello!".encode())
except KeyboardInterrupt:
	ser.close()

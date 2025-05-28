import serial
import threading

# CHANGE THIS ACCORDING TO YOUR PLATFORM
PORT = '/dev/ttyAMA0'   # Raspberry Pi
# PORT = 'COM3'         # Windows

BAUDRATE = 9600

def read_from_uart(ser):
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print(f"\n[Received] {line}")
            except Exception as e:
                print(f"Error reading: {e}")

def write_to_uart(ser):
    while True:
        try:
            user_input = input("[Send] Type message: ")
            ser.write((user_input + "\n").encode('utf-8'))
        except Exception as e:
            print(f"Error writing: {e}")

def main():
    try:
        ser = serial.Serial(PORT, BAUDRATE, timeout=1)
        print(f"Opened serial port {PORT} at {BAUDRATE} baud.")

        # Start read and write threads
        reader = threading.Thread(target=read_from_uart, args=(ser,), daemon=True)
        writer = threading.Thread(target=write_to_uart, args=(ser,), daemon=True)

        reader.start()
        writer.start()

        # Keep main thread alive
        while True:
            pass

    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"Failed to open serial port: {e}")
    finally:
        ser.close()

if __name__ == '__main__':
    main()


# Serial Communication Protocols Comparison

## 📊 Comparison Table

| Feature                        | **UART (Universal Asynchronous Receiver/Transmitter)** | **SPI (Serial Peripheral Interface)**   | **I2C (Inter-Integrated Circuit)**       |
|-------------------------------|--------------------------------------------------------|-----------------------------------------|------------------------------------------|
| **Communication Type**        | Asynchronous                                           | Synchronous                              | Synchronous                               |
| **No. of Wires**              | 2 (TX, RX)                                             | 4 (MOSI, MISO, SCLK, SS/CS)              | 2 (SDA, SCL)                              |
| **Speed**                     | Up to 1 Mbps (typical)                                 | Up to tens of Mbps (very fast)           | Up to 3.4 Mbps (in high-speed mode)       |
| **Full/Duplex**               | Full-Duplex                                            | Full-Duplex                              | Half-Duplex                               |
| **Master-Slave**              | Peer-to-peer                                           | One master, multiple slaves              | Multi-master, multi-slave                 |
| **Addressing**                | No (direct peer-to-peer)                               | No (individual SS lines per slave)       | Yes (uses unique addresses per device)    |
| **Clock Required**            | No                                                     | Yes (provided by master)                 | Yes (provided by master)                  |
| **Data Acknowledgment**       | No                                                     | No                                       | Yes (ACK/NACK)                            |
| **Complexity**                | Simple                                                 | Moderate (more wires, manual SS)         | More complex (addressing, protocol logic) |
| **Use Case**                  | GPS, Bluetooth modules, basic serial logging           | Display drivers, flash memory, sensors   | Real-time clocks, EEPROM, multiple sensors|
| **Distance**                  | Short to moderate (few meters)                         | Short (typically < 1 meter)              | Short (up to a few meters)                |
| **No. of Devices**            | 2 (one TX, one RX)                                     | Limited by available SS pins             | 1008 slaves (theoretically)               |

## ✅ Recommendations

- **Use UART** when:  
  You need simple, low-speed, peer-to-peer communication (e.g., debugging, GPS modules).

- **Use SPI** when:  
  Speed is critical and you have few devices (e.g., OLED displays, flash memory).

- **Use I2C** when:  
  You want to connect many low-speed peripherals with fewer pins (e.g., sensors, RTCs).

# HabitatMonitor

**HabitatMonitor** is an IoT project designed to monitor environmental conditions in a habitat using a network of ESP32 microcontrollers. Each ESP32 node collects data from connected sensors and sends it to a central Flask server for aggregation and display.

## Features

- **Temperature and Humidity Monitoring**: Uses DHT22 sensors to measure temperature and humidity.
- **Soil Moisture Monitoring**: Uses soil moisture sensors to monitor soil conditions.
- **Wireless Data Transmission**: Utilizes the ESP32’s Wi-Fi capabilities to send sensor data to a remote server.
- **MicroPython on ESP32**: Leverages MicroPython for easy and efficient development on the ESP32.
- **Flask Server with WebSocket**: Implements a Flask server to receive, process, and display the data with real-time updates using WebSocket.
- **Real-Time Data Visualization**: Displays the collected data on a web interface.

## Components

- **ESP32 Development Boards**
- **DHT22 Temperature and Humidity Sensors**
- **Soil Moisture Sensors**
- **Power Supply (e.g., battery packs for each ESP32)**
- **Wi-Fi Network**
- **Central Server (e.g., Raspberry Pi or any server running Flask)**
- **Cables and Connectors**

## Setup

### ESP32 Nodes

1. **Flash MicroPython firmware to your ESP32.**
2. **Upload `main.py` to your ESP32 using a tool like `ampy` or `mpfshell`.**
   ```bash
   ampy --port /dev/ttyUSB0 put main.py


import network
import urequests
import time
from machine import Pin, ADC
import dht

# Replace with your network credentials
SSID = 'your_SSID'
PASSWORD = 'your_PASSWORD'

# Replace with your Flask server IP and port
SERVER_URL = 'http://your_server_ip:5000/data'

# Initialize DHT22 sensor
dht_pin = Pin(4)
sensor = dht.DHT22(dht_pin)

# Initialize soil moisture sensor
soil_moisture_pin = ADC(Pin(34))

# Connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        time.sleep(1)
    
    print('Connected to WiFi')
    print('IP:', wlan.ifconfig()[0])

# Read from sensors and send data to the server
def read_and_send_data(node_id):
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        soil_moisture = soil_moisture_pin.read()  # Read soil moisture value
        print(f'Node {node_id} - Temperature: {temperature} °C, Humidity: {humidity} %, Soil Moisture: {soil_moisture}')

        data = {
            'node_id': node_id,
            'temperature': temperature,
            'humidity': humidity,
            'soil_moisture': soil_moisture
        }
        response = urequests.post(SERVER_URL, json=data)
        print('Response:', response.text)
        response.close()
    except Exception as e:
        print('Failed to read sensor or send data:', e)

def main():
    node_id = 'node_1'  # Unique ID for this node
    connect_wifi(SSID, PASSWORD)
    while True:
        read_and_send_data(node_id)
        time.sleep(10)

if __name__ == '__main__':
    main()

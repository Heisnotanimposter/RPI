import network
import urequests
import time
from machine import Pin, I2C
import dht

# Connect to Wi-Fi
ssid = 'your_wifi_ssid'
password = 'your_wifi_password'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    time.sleep(1)

print('Connection successful')
print(wlan.ifconfig())

# Setup DHT sensor (example for DHT11)
sensor = dht.DHT11(Pin(14))

def read_sensor():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    return temp, hum

# Send data to server
url = "http://your_server_ip:5000/data"
while True:
    temp, hum = read_sensor()
    data = {'temperature': temp, 'humidity': hum}
    response = urequests.post(url, json=data)
    print(response.text)
    time.sleep(60)  # Send data every 60 seconds
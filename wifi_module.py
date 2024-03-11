import network

# Define the WiFi network credentials
WIFI_SSID = "Wi_KNUT"
WIFI_PASSWORD = ""

# Connect to the WiFi network
wlan = network.WLAN(network.STA_IF)
wifi.active(True)
#wifi.connect(WIFI_SSID, WIFI_PASSWORD)
accesspoints = wlan.scan()

# Wait for the Pico to connect to the WiFi network
#while not wifi.isconnected():
#    pass

# Print the IP address assigned to the Pico
#print("IP address:", wifi.ifconfig()[0])

for ap in accesspoints:
    print(ap)
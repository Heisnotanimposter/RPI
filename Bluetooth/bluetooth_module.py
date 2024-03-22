import micropython
micropython.alloc_emergency_exception_buf(100)

from ble_advertising import advertising_payload
from ble import BLE

# Define the service UUID and characteristic UUID
SERVICE_UUID = b'12345678-1234-5678-1234-56789abcdef0'
CHARACTERISTIC_UUID = b'12345678-1234-5678-1234-56789abcdef1'

# Define the advertising data
adv_payload = advertising_payload(name='Pico W', services=[SERVICE_UUID])

# Define the BLE object
ble = BLE()

# Define the characteristic write callback function
def write_callback(data):
    print("Received data:", data)

# Define the BLE service and characteristic
ble.config(name='Pico W', tx_power=4, adv_payload=adv_payload)
ble.add_service(SERVICE_UUID)
ble.add_characteristic(CHARACTERISTIC_UUID, properties=BLE.WRITE, write_callback=write_callback)

# Start advertising
ble.start_advertising()

# Loop forever
while True:
    # Send data to the central device
    data = "Hello, Bluetooth!"
    ble.update_characteristic_value(CHARACTERISTIC_UUID, data)

    # Wait for 1 second
    time.sleep(1)

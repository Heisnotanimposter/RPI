import machine
import time

# Define the pin numbers for the ultrasonic sensor and buzzer
TRIG_PIN = 2
ECHO_PIN = 3
BUZZER_PIN = 4

# Create machine.Pin objects for the sensor and buzzer pins
trig_pin = machine.Pin(TRIG_PIN, machine.Pin.OUT)
echo_pin = machine.Pin(ECHO_PIN, machine.Pin.IN)
buzzer_pin = machine.Pin(BUZZER_PIN, machine.Pin.OUT)

# Define a function to measure the distance using the ultrasonic sensor
def measure_distance():
    # Send a 10us pulse to the TRIG pin
    trig_pin.value(1)
    time.sleep_us(10)
    trig_pin.value(0)

    # Wait for the ECHO pin to go high
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()

    # Wait for the ECHO pin to go low
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()

    # Calculate the duration of the pulse
    pulse_duration = pulse_end - pulse_start

    # Calculate the distance in centimeters
    distance = pulse_duration / 58.0

    return distance

# Loop forever
while True:
    # Measure the distance using the ultrasonic sensor
    distance = measure_distance()

    # Check the distance and adjust the sleep time
    if distance < 5:
        sleep_time = 0.05
    elif distance < 10:
        sleep_time = 0.1
    elif distance < 20:
        sleep_time = 0.2
    else:
        sleep_time = 0.5

    # Check if the distance is less than 5 cm
    if distance < 5:
        # Turn on the buzzer and emit a beep sound
        buzzer_pin.value(1)
        time.sleep(0.1)
        buzzer_pin.value(0)
        time.sleep(0.1)
    else:
        # Turn off the buzzer
        buzzer_pin.value(0)

    # Wait for the appropriate sleep time
    time.sleep(sleep_time)
    
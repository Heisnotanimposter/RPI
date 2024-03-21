
### Arduino Robotics Project




https://github.com/Heisnotanimposter/Arduino/assets/97718938/34024e8d-4e5f-4a68-affb-04628383b8c7


```markdown
# Autonomous 2-Wheel Robot Project

## Overview
This project is an autonomous 2-wheel robot designed to navigate environments independently. It utilizes microwave sensors for obstacle avoidance, ensuring safe and efficient movement through its surroundings. The robot features Bluetooth connectivity for communication and control, and it can connect over HTTPS to a user's smartphone, allowing for remote monitoring and operation.

## Key Features
- **Obstacle Avoidance**: Uses microwave sensors to detect and navigate around obstacles.
- **Bluetooth Connectivity**: Enables communication and control through a Bluetooth module.
- **HTTPS Connection**: Allows for remote interaction with the robot via a user's smartphone.
- **Motor Control**: Manages the robot's movement with precise motor control.

## Project Structure
- `.gitattributes` & `.DS_Store`: Git and system files.
- `Embeddedmain.py`: The main script running on the robot, coordinating its operations.
- `ble_advertising.py`: Manages Bluetooth Low Energy (BLE) advertising for discovery by other devices.
- `bluetooth_module.py`: Handles Bluetooth communication, including pairing and data exchange.
- `distance_measure.py`: Interacts with the microwave sensor for distance measurement and obstacle detection.
- `motor_test.py`: Tests and calibrates the motors controlling the robot's wheels.
- `wifi_module.py`: Manages the WiFi connection for HTTPS communication with the smartphone app.

## Getting Started

### Prerequisites
- Arduino board (model specified here)
- Microwave sensor (model specified here)
- Bluetooth module (model specified here)
- WiFi module (for HTTPS communication)
- Motors and wheels setup
- Smartphone with the companion app installed

### Installation
Provide detailed instructions on how to assemble the robot, upload the code to the Arduino board, and any additional setup required for the Bluetooth, WiFi, and microwave sensor components.

## Usage
Explain how to start the robot, establish a Bluetooth connection with a smartphone, and use the companion app to control the robot or receive data from it.

## Contributing
We welcome contributions to this project! Please refer to the contributing guidelines for more information on how to propose improvements or report issues.

## License
Specify the license under which this project is released.

## Acknowledgments
- Credit any individuals or resources that have assisted in the development of this project.
```

**IoT Device Reference Application**
==================
The example IoT Device Reference application implemented in a Raspberry Pi 3 and Sense HAT reads IoT data from the Sense HAT and posts this data to the IoT Services Reference application using its published REST API's. These applications in combination demonstrate a simple, scalable, Cloud based IoT application.

![IoT Device](https://github.com/markreha/cloudworkshop/blob/master/sdk/docs/architecture/images/iotdevice.png)

Architecture & Technologies
--------
 The IoT Device Reference application is designed and implemented in Python using the Sense HAT API's included in the Raspbian OS image. 

The [IoT Sense HAT](http://pythonhosted.org/sense-hat/) supports the following features:

 - Temperature, Humidity, and Barometric pressure 
 - Gyroscope Accelerometer, and Magnetometer
 - LED display 
 - Joystick 
 
Basic Application Functionality
--------
The IoT Device Reference application, as show in the flow chart below, primary functionality includes sitting in loop reading the Sense HAT IoT data, posting this data to server using a REST API, and then sleeping for a specified period of time. The current IoT Device Reference application leverages the LED display and the Temperature, Humidity, and Barometric pressure sensors in its implementation. The application could be extended in the future to leverage other features of the Sense HAT.

![IoT Device Flow Chart Diagram](https://github.com/markreha/cloudworkshop/blob/master/sdk/docs/architecture/images/iotrestservice.png)

Repository Contents
----------
This repository contains code to support Raspberry Pi 3 and Sense HAT or a Raspberry Pi 3 DHT11 and LED wired to a breadboard. The IoT Device Reference application can be used as a starting point to monitor Weather IoT data.

 - ***app/hat***: this folder contains the Python 3 code for the Reference IoT Device application using a Sense HAT.
 - ***app/discrete***: this folder contains the Python 3 code for the Reference IoT Device application using the DHT11 and LED discrete components.

[Back to Top](#iot-device-reference-application)

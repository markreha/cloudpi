**Raspberry Pi IoT Device Reference Application**
==================
The example IoT Device Reference application implemented in a Raspberry Pi 3 and Sense HAT reads IoT data from the Sense HAT and posts this data to the IoT Services Reference application using its published REST API's. These applications in combination demonstrate a simple, scalable, Cloud based IoT application. Get the [Cloud Workshop SDK!](https://github.com/markreha/cloudworkshop/blob/master/README.md)

<p align="center">
	<img src="https://github.com/markreha/cloudworkshop/blob/master/sdk/docs/architecture/images/iotdevice.png" alt="IoT Device"/>
</p>

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
The IoT Device Reference application logic, as illustrated in the flow chart below, primary functionality includes sitting in loop reading the Sense HAT IoT data, posting this data to the IoT Services application using a REST API, and then sleeping for a specified period of time. The current IoT Device Reference application leverages the LED display and the Temperature, Humidity, and Barometric pressure sensors in its implementation. The application uses the Logging Framework built into the Python 3 libraries. The application could be extended in the future to leverage other features of the Sense HAT.

It should be noted that the IoT Device Reference application contains additional logic so that the Raspberry Pi and Sense HAT could be shared across multiple back end IoT Services applications with the assumption that each back end adheres to the REST API as defined in this SDK. The REST API endpoints are configured in the Config.py code module.

![IoT Device Flow Chart Diagram](https://github.com/markreha/cloudworkshop/blob/master/sdk/docs/architecture/images/iotflowchart.png)

Application Configuration
--------
The IoT Device Reference application can be configured thru a number of constants in the Config.py code module. To configure the IoT Device Reference application perform the following steps:
1) Set the 'environment' variable to either dev1, dev2, qa, or prod to post to a desired IoT Services back-end environment.
2) Set the 'sampleTime' variable to the number of milliseconds to sample the weather sensors.
3) Set the IoT Services REST API primary URL endpoint and credentials for the envirnment set in step 1.
4) Set optional IoT Services REST API secondary URL endpoints, which can be used to support additional environments and cloud platforms.

Repository Contents
----------
This repository contains code to support the Raspberry Pi 3 and Sense HAT or a Raspberry Pi 3 along with discrete DHT11 and LED components wired to a breadboard. The IoT Device Reference application can be used as a starting point to monitor Weather IoT data. To run this code on your Raspberry Pi 3 simply clone this repository to your device and customize the configuration as nessarary for your backend REST API's.

 - ***app/hat***: this folder contains the Python 3 code for the Reference IoT Device application using a Sense HAT.
 - ***app/discrete***: this folder contains the Python 3 code for the Reference IoT Device application using the DHT11 and LED discrete components.

[Back to Top](#iot-device-reference-application)

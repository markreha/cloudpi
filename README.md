**IoT Device Reference Application**
==================
The example IoT Device Reference application implemented in a Raspberry Pi and Sense HAT reads IoT data from the Sense HAT and posts this data to the IoT Services Reference application using its published REST API's. These applications in combination demonstrate a simple, scalable, Cloud based IoT application.

![IoT Device](https://github.com/markreha/cloudworkshop/blob/master/sdk/docs/architecture/images/iotdevice.png)

Architecture & Technologies
--------
 The IoT Services Reference application is designed and implemented in Java using the Spring Framework (Spring Core and Spring JDBC) that implements its published REST API's based on the JAX-RS framework using the Jackson and Jersey implementation libraries. 
 
REST API's
--------
The IoT Services Reference application publishes 3 API's, one of which is an API used for testing and the remaining 2 API's to save and retrieve IoT Weather Data. It should be noted that the REST endpoint is secured by using HTTPS and Basic HTTP Authentication. All REST API's are based off of the [hostname]/cloudservices/weather URL.

![IoT Services UML Diagram](https://github.com/markreha/cloudworkshop/blob/master/sdk/docs/architecture/images/iotrestservice.png)

The REST API's include:

 - GET at /test: will return a test string and is used to test the endpoint
 - GET at /get: will return IoT Weather data for a specified Device ID, From Date, and End Date
 - POST at /save: will save IoT Weather data from the a specified WeatherSensorModel

from sense_hat import SenseHat
import Config as cfg
import os
import sys
import datetime
import json
import requests
import time
import logging
import logging.handlers

# Create an instance of the Sensor HAT
sense = SenseHat()
pixel_location = 0

############# HELPER FUNCTIONS ###################

# Startup screen
def startupScreen():
    # Clear display
    sense.clear()
    sense.set_rotation(180)

    # Display startup text
    sense.show_letter('G', text_colour=(100, 50, 150))
    time.sleep(2)
    sense.show_letter('C', text_colour=(255, 255, 255))
    time.sleep(2)
    sense.show_letter('U', text_colour=(100, 50, 150))
    time.sleep(2)
    sense.clear()
    
# Get the CPU Temperature
def getCpuTemp():
    ms = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cputemp = ms.read()
    cputemp = cputemp.replace('temp=','')
    cputemp = cputemp.replace('\'C\n','')
    return float(cputemp)

# Get the Current Temperature
def getCurrentTemp():
    # Get temp from sensor, convert temp to Farenheit and apply a fudge factor
    fudge = 2
    t = sense.get_temperature() - fudge
    return t

# Convert Temperature from C to F
def temperatureCtoF(temp):
    return (temp * 9/5) + 32    

# Convert Presure from Mb to In
def pressureMbtoIn(pressure):
    return pressure/33.8638    

# Turn Indicator light on and off
def indicator(state, error):
    if error:
        color = (255, 0, 0)
    else:
        color = (0, 255, 0)
    if state:
        sense.show_letter('*', text_colour=color)
    else:
        sense.show_letter(' ', text_colour=color)

# Turn a Pixel on
def pixel(error):
    global pixel_location
    if pixel_location == 64:
        pixel_location = 0
        sense.clear()
    if error:
        color = (255, 0, 0)
    else:
        if pixel_location & 1:
            color = (255, 255, 255)
        else:
            color = (100, 50, 150)
    sense.set_pixel(pixel_location & 0x07, int(pixel_location / 8), color)
    pixel_location = pixel_location + 1
    

#################################################

# Setup log file for application
log = logging.handlers.TimedRotatingFileHandler('sensor.log', 'midnight', 5)
log.doRollover()
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)
logger.addHandler(log)

# Load the current Environment Configuration
print("IoT Weather Application v0.1")
if cfg.environment == "dev1":
    print("Running Dev 1 Environment Configuration")
    logger.info("Running Dev 1 Environment Configuration")
    environment = cfg.env_dev1
elif cfg.environment == "dev2":
    print("Running Dev 2 Environment Configuration")
    logger.info("Running Dev 2 Environment Configuration")
    environment = cfg.env_dev2
elif cfg.environment == "qa":
    print("Running QA Environment Configuration")
    logger.info("Running QA Environment Configuration")
    environment = cfg.env_qa
else:
    print("Running Production Environment Configuration")
    logger.info("Running Production Environment Configuration")
    environment = cfg.env_prod

# Application constants from Environment and Configuration file
sampleTime = cfg.sampleTime
deviceID = cfg.deviceID
webApiUrl = environment["webApi"]
webApiUsername = environment["username"]
webApiPassword = environment["password"]

# Display Startup Screen
startupScreen()

# Dictionary to hold Temperature Sensor data
temperatureData = {}

# Sit in a loop reading the sensors every sampleTime, convert result to JSON, and POST to the Web API
while True:
    # Print running indicator to console
    print('.', end='')
    sys.stdout.flush()
    
    # Get current temp, pressure, and humidity
    t = getCurrentTemp()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round all values and then display
    t = round(temperatureCtoF(t), 2)
    p = round(pressureMbtoIn(p), 2)
    h = round(h, 2)

    # Save the Temperature Sensor results in a Temperature Data Object
    temperatureData["deviceID"] = deviceID
    temperatureData["temperature"] = t
    temperatureData["humidity"] = h
    temperatureData["pressure"] = p

    # Log sensor data
    msg = "Sampled at {0}  Temperature = {1}F, Pressure = {2}In, Humidity = {3}%".format(str(datetime.datetime.now()),t,p,h)
    logger.debug(msg)

    # Convert the Temperature Data Object to JSON string
    strj = json.dumps(temperatureData, ensure_ascii=False)

    # POST the JSON results to the RESTful Web API using HTTP Basic Authentication
    response = requests.post(webApiUrl, strj, headers={'Content-Type':'application/json'}, auth=(webApiUsername, webApiPassword))
    if response.status_code == 200:
        #indicator(True, False)
        pixel(False)
        strj = response.json()
        logger.info("Response status is %s with message of %s" % (strj["status"], strj["message"]))
    else:
        #indicator(True, True)
        pixel(True)
        logger.error("Response error with status code of %d" % response.status_code)
    time.sleep(2)
    
    # Sleep until we need to read the sensors again
    time.sleep(sampleTime)


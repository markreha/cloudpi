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

# Turn a Pixel on, -1 is HTTP Exception, 0 is no Error, 1 is primary endpoint error, 2 is secondary endpoint error
def pixel(error):
    global pixel_location
    if pixel_location == 64:
        pixel_location = 0
        sense.clear()
    if error > 1:
        color = (255, 165, 0)
    elif error == 1:
        color = (255, 0, 0)
    elif error == 0:
        if pixel_location & 1:
            color = (255, 255, 255)
        else:
            color = (100, 50, 150)
    else:
        color = (0, 255, 0)
    sense.set_pixel(pixel_location & 0x07, int(pixel_location / 8), color)
    pixel_location = pixel_location + 1
    
# Post Data to the Primary Endpoint and return count of unsuccessful posts
def post_primary_endpoint(webApiUrl, webApiUsername, webApiPassword, strj):
    # POST the JSON results to the RESTful Web API using HTTP Basic Authentication
    response = requests.post(webApiUrl, strj, headers={'Content-Type':'application/json'}, auth=(webApiUsername, webApiPassword))
    if response.status_code == 200:
        strj = response.json()
        logger.info("Response status is %s with message of %s" % (strj["status"], strj["message"]))
        return 0
    else:
        logger.error("Response error with HTTP status code of %d" % response.status_code)
        return 1

# Post Data to the Secondary Endpoints and return the count of unsuccessful posts
def post_secondary_endpoint(secondary_endpoints, strj):
    # POST the JSON results to the Secondary Endpoints
    status = 0
    if process_secondary_endpoints:
        for i in range(len(secondary_endpoints)):
            response = requests.post(secondary_endpoints[i][1], strj, headers={'Content-Type':'application/json'}, auth=(secondary_endpoints[i][2], secondary_endpoints[i][3]))
            if response.status_code == 200:
                strjResponse = response.json()
                logger.info("   Sent data to %s Secondary Endpoint sucessful with response status of %s with message of %s" % (secondary_endpoints[i][0], strjResponse["status"], strjResponse["message"]))
            else:
                logger.error("   Sent data to %s Secondary Endpoint failed with HTTP status code of %d" % (secondary_endpoints[i][0], response.status_code))
                status += 1
    return status
            
#################################################

# Setup log file for application
log = logging.handlers.TimedRotatingFileHandler('sensor.log', 'midnight', 5)
log.doRollover()
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)
logger.addHandler(log)

# Load the current Environment Configuration
print("IoT Weather Application v0.3")
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
secondary_endpoints = cfg.sec_endpoints
process_secondary_endpoints = cfg.process_sec_endpoints

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
    strj = json.dumps(temperatureData, ensure_ascii=True)

    try:
        # POST the JSON results to the Primary Endpoint
        status1 = post_primary_endpoint(webApiUrl, webApiUsername, webApiPassword, strj)
    
        # POST the JSON results to the Secondary Endpoints
        status2 = post_secondary_endpoint(secondary_endpoints, strj)

        # Display Status LED
        if status2 != 0:
            pixel(2)
        elif status1 == 1: 
            pixel(1)
        else:
            pixel(0)
    except:
        # Log exception and update Status LED
        logger.error("   Error: HTTP exception caught.")
        pixel(-1)
            
    # Sleep until we need to read the sensors again
    time.sleep(sampleTime)


import RPi.GPIO as GPIO
import dht11_lib
import time
import datetime
import json
import requests

# Application constants
sampleTime = 20
debug = True
#webApiUrl = "http://marks-macbookair.local:8080/workshop/rest/dht11/save"
webApiUrl = "http://node5.codenvy.io:37551/cloudservices/rest/dht11/save"
#webApiUrl = "http://cloud-services-playlaravel.44fs.preview.openshiftapps.com/cloadservices/rest/dht11/save"
webApiUsername = "CloudWorkshop"
webApiPassword = "dGVzdHRlc3Q="

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Read data from sensor on GPIO pin 4
instance = dht11_lib.DHT11(pin=4)

# Sit in a loop reading the sensor every sampleTime, convert result to JSON, and POST to our Web API
data = {}
while True:
    # Read the sensor
    result = instance.read()
    if result.is_valid():
        # Get results
        now = str(datetime.datetime.now())
        tempC = result.temperature
        tempF = (result.temperature * 9/5 + 32)
        humidity = result.humidity
        
        # Print results to the console
        if debug:
            print("Sampled at %s  Temperature: %.2f C %.2f F Humidity: %.2f" % (now, tempC, tempF, humidity))

        # Save results to a data object
        data["deviceID"] = 0
        data["temperature"]= tempF
        data["humidity"] = humidity

        # Convert data object to JSON
        strj = json.dumps(data, ensure_ascii=False)

        # POST the JSON results to the RESTful Web API
        response = requests.post(webApiUrl, strj, headers={'Content-Type':'application/json'}, auth=(webApiUsername, webApiPassword))
        if response.status_code == 200:
            strj = response.json()
            print("Response status is %s with message of %s" % (strj["status"], strj["message"]))
        else:
            print("Response Error: %d" % response.status_code)

    # Sleep until we need to read the sensor again
    time.sleep(sampleTime)

import RPi.GPIO as GPIO
import time

# Initialize GPIO for Pin 17
print("Starting LED and GPIO test...........")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

# Turn LED On
GPIO.output(17,GPIO.HIGH)
print("LED on")
time.sleep(5)

# Turn LED Off
GPIO.output(17,GPIO.LOW)
print("LED off")
time.sleep(5)

# Turn LED On
GPIO.output(17,GPIO.HIGH)
print("LED on")
print("Completed LED and GPIO test")




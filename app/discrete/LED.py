import RPi.GPIO as GPIO

class LED:
	def __init__(self, gpioPin):
		self.__gpioPin = gpioPin
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(gpioPin,GPIO.OUT)
		
	def on(self):
		GPIO.output(self.__gpioPin,GPIO.HIGH)

	def off(self):
		GPIO.output(self.__gpioPin,GPIO.LOW)

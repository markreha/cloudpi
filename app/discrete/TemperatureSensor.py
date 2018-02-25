import dht11_lib

class TemperatureSensor:
	@property
	def valid(self):
		return self.__valid
        
	@property
	def temperatureC(self):
		return self.__temperatureC

	@property
	def temperatureF(self):
		return self.__temperatureF
        
	@property
	def humidity(self):
		return self.__humidity
        
	def __init__(self, gpioPin):
		self.__instance = dht11_lib.DHT11(pin=gpioPin)
		self.__valid = False
		self.__temperatureC = 0
		self.__temperatureF = 0
		self.__humidity = 0	
		
	def read(self):
		result = self.__instance.read()
		self.__valid = result.is_valid()
		self.__temperatureC = result.temperature
		self.__temperatureF = (result.temperature * 9/5 + 32)
		self.__humidity = result.humidity	

import os
from sense_hat import SenseHat
sense = SenseHat()

def getCpuTemp():
    ms = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cputemp = ms.read()
    cputemp = cputemp.replace('temp=','')
    cputemp = cputemp.replace('\'C\n','')
    return float(cputemp)

def getCurrentTemp():
    global fudge
#    fudge = 1.5
#    t1 = sense.get_temperature_from_humidity()
#    t2 = sense.get_temperature_from_pressure()
#    t = (t1 + t2)/2
    fudge = 2.8
    t = sense.get_temperature()
    return t

def temperatureCtoF(temp):
    return (temp * 9/5) + 32    

def pressureMbtoIn(pressure):
    return pressure/33.8638    

while True:
    # Get current temp, pressure, and humidity
    t = getCurrentTemp()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Convert temp to Farenheit and apply Sensor HAT correction forumla
    t = t - ((getCpuTemp() - t)/fudge)    

    # Round all values and then display
    t = round(temperatureCtoF(t), 2)
    p = round(pressureMbtoIn(p), 2)
    h = round(h, 2)
    msg = "Temperature = {0}F, Pressure = {1}In, Humidity = {2}%".format(t,p,h)
#    sense.show_message(msg, scroll_speed=0.05)
    print(msg)

import machine
import urequests 
from machine import Pin, ADC
import network, utime
#from dht import DHT11, InvalidChecksum
sensor = ADC(Pin(26)) 

HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'YQUN3GRV1ZFERUB5'  
 
ssid = 'IZZI-3E86-5G'
password = 'A811FC233E86'
 
# Configure Pico W as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
 
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 
 
while True:
    utime.sleep(5)
    utime.sleep(5)
    utime.sleep(5)
#    pin = Pin(0, Pin.OUT, Pin.PULL_DOWN)
    sensor_value = sensor.read_u16()
    temp= sensor_value*(3.3/65535)
    temp = temp/0.010
    #sensor = DHT11(pin)
    #t  = (sensor.temperature)
    #h = (sensor.humidity)
    print("Temperature: {}".format(temp))
    #print("Humidity: {}".format(sensor.humidity))
    
    dht_readings = {'field1':temp}#, 'field2':h} 
    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = dht_readings, headers = HTTP_HEADERS )  
    request.close() 
    print(dht_readings)
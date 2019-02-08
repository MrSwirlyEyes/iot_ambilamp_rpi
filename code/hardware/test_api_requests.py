import time
import requests

from libraries.DHT22 import DHT22
from libraries.MCP300X import MCP300X


dht22_pin=5
dht22 = DHT22(dht22_pin)


mcp3004 = MCP300X.MCP3004
mcp = MCP300X(mcp3004)

ldr = mcp.CH2

url='http://intro-to-iot.herokuapp.com/api/data'

packet = {}

delay = 10 * 60

while True:


    temperature, humidity = dht22.get_temperature_and_humidity()

    brightness = mcp.read(ldr)

    packet['temperature'] = round(temperature, 3)
    packet['humidity'] = round(humidity, 3)
    packet['brightness'] = brightness

    #print(packet)

    r = requests.post(url,json=packet)

    time.sleep(delay)

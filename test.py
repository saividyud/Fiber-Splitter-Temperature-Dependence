import board
from adafruit_bme280 import basic as adafruit_bme280
import time as t
import numpy as np
import pandas as pd

i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

ground_pressure = bme280.pressure
print('Ground pressure: {ground_pressure:.2f} hPa')

# Setting sea level pressure
bme280.sea_level_pressure = ground_pressure

try:
    while True:
        temp = bme280.temperature
        pres = bme280.pressure
        hum = bme280.humidity
        alt = bme280.altitude
        print(f'Temperature: {temp:.2f} C, Pressure: {pres:.2f} hPa, Humidity: {hum:.2f}%, Altitude: {alt:.2f} m')
        
        t.sleep(0.5)
except Exception as e:
    print(f'Exception encountered: {e}')
import board
from adafruit_bme280 import basic as adafruit_bme280
import time as t
import numpy as np
import pandas as pd
import csv

i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

ground_pressure = bme280.pressure
print(f'Ground pressure: {ground_pressure:.2f} hPa')

# Setting sea level pressure
bme280.sea_level_pressure = ground_pressure

num_data_points = 5000
file = open('Data Files/2026-07-23/data_2.csv', 'w')
writer = csv.writer(file)

headers = ['Time [s]', 'Temperature [C]', 'Pressure [Pa]', 'Humidity [%]', 'Altitude [m]']
writer.writerow(headers)

start_time = t.time()

try:
    for i in range(num_data_points):
        current_time = t.time() - start_time
        temp = bme280.temperature
        pres = bme280.pressure
        hum = bme280.humidity
        alt = bme280.altitude
        print(f'{i} | Time: {current_time:.2f} s, Temperature: {temp:.2f} C, Pressure: {pres:.2f} hPa, Humidity: {hum:.2f}%, Altitude: {alt:.2f} m')
        
        data = [current_time, temp, pres, hum, alt]
        writer.writerow(data)
        
        t.sleep(0.3)
        
    print('Iterations completed!')
    print('Closing file')
    file.close()
    print(f'Total time: {(t.time() - start_time):.2f} s')

except KeyboardInterrupt:
    print(f'Program manually stopped!')
    print('Closing file')
    file.close()
    
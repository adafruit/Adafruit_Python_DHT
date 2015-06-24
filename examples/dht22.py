#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Eric Dufresne

import Adafruit_DHT
import time

class Temperature():
    def __init__(self, rawTempData):
        self.rawTempData = rawTempData
        
    @property
    def C(self):
        return self.rawTempData
        
    @property
    def F(self):
        return self.C * 9.0 / 5.0 + 32.0

class Humidity():
    def __init__(self, rawHumidityData):
        self.rawHumidityData = rawHumidityData
        
    @property
    def Pourcent(self):
        return float(self.rawHumidityData)

class DhtSensorController():
    def __init__(self, sensorType, gpioPin):
        self.sensorType = sensorType
        self.gpioPin = gpioPin
        
    def readData(self):
        if self.sensorType == 11:
            sensor = Adafruit_DHT.DHT11
        elif self.sensorType == 22:
            sensor = Adafruit_DHT.DHT22
        elif self.sensorType == 23:
            sensor = Adafruit_DHT.AM2302
        else:
            self.readSuccess = False
            raise Exception("Unknow sensor type. Use 11 for DHT11, 22 for DHT22 and 23 for AM2302")

        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, self.gpioPin)
        if humidity is not None and temperature is not None:
            self.temperature = Temperature(temperature)
            self.humidity = Humidity(humidity)
            self.readSuccess = True
        else:
            self.readSuccess = False
            raise Exception('Failed to get reading. Try again!')

if __name__ == "__main__":
    try:
        # Specs DHT22 and AM2302
        # http://akizukidenshi.com/download/ds/aosong/AM2302.pdf
        print("Relative humidity sensor performance.")
        print("Resolution: 0.1%RH.")
        print("Range: 0%RH to 99,9%RH.")
        print("Accuracy: At 25°C, ±2%RH.")
        print("Drift: <0,5%RH/yr.")
        print()
        print("Temperature sensor performance.")
        print("Resolution: 0,1°C.")
        print("Accuracy: ±0,5°C.")
        print("Range: -40°C to +80°C.")
        print("Drift: ±0,3°C/yr.")
        print()
        print("Electrical characteristics.")
        print("Voltage: 3,3V to 5,5V.")
        print("Power consumption: Dormancy 15μA, Measuring 500μA.")
        print("Sampling period: 2S.")
        print()

        # Objet instance.
        # Arg1: DHT type.
        #       DHT11 = 11
        #       DHT22 = 22
        #       AM2302 = 23
        # Arg2: Raspberry Pi 2 GPIO pin
        dht = DhtSensorController(22,4)
        
        while True:
            # Read data.
            dht.readData()
        
            # Read Success?
            print("Success?", dht.readSuccess)
        
            # Print data.
            print("%.1f Celsius." % dht.temperature.C)
            print("%.1f Fahrenheit." % dht.temperature.F)
            print("%.1f %% relative humidity." % dht.humidity.Pourcent)
            print()

            # Sampling period for next data read
            time.sleep(5)
    except KeyboardInterrupt:
        print("Interrupt by user.")
        exit
    except Exception as e:
        print("Exeption error.\n", e)
        raise
    finally:
        dht = None
        print("End.")
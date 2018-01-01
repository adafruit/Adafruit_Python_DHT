#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import Adafruit_DHT
import argparse

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor_map = {
    'dht11': Adafruit_DHT.DHT11,
    'dht22': Adafruit_DHT.DHT22,
    'am2302': Adafruit_DHT.AM2302,
}

def read_sensor(sensor, pin):
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Read sensors from DHT22/DHT11/AM2302')
    parser.add_argument('--sensor', default='dht22', help="Sensor type. One of 'dht11', 'dht22', 'am2302' (default: dht22)")
    parser.add_argument('--pin', default=17, help="Pin for sensor (e.g. 'P8_11' for Beaglebone Black, '17' for Raspberry Pi GPIO17) (default=17)")

    args = parser.parse_args()

    if args.sensor not in ['dht11', 'dht22', 'am2302']:
        print "Must specify one of 'dht11', 'dht22', am2302. You specified: %s" % (args.sensor)

    # Attempt to set the pin to an integer for Raspberry Pi GPIO values.
    pin = ''
    try:
        pin = int(args.pin)
    except ValueError:
        pin = args.pin

    read_sensor(sensor_map[args.sensor], pin)

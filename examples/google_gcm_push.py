#!/usr/bin/python
# Copyright (c) 2015 Younghwan Jang
# Author : Younghwan Jang with modifying Tony DiCola's code, 2014 Adafruit Industries
# See https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py

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


import sys

import Adafruit_DHT

import subprocess, httplib, json, datetime, time

# Global Variables

# This program pushes to your Android device if the sensor senses
# lower or higher temperature or humidity than what you specified.


# This example needs Google Cloud Messaging service.
# You need to get a server API key from Google Developer Console,
# (https://console.developers.google.com/)
# and a GCM device's ID which is created on the Android device side.
# Please take a look at the following URL to see in detail:
# (https://developer.android.com/google/gcm/)
GCM_SERVER_API_KEY = 'YOUR GCM SERVER API KEY'
GCM_REQUEST_URL = 'android.googleapis.com'
GCM_REQUEST_SUBPATH = '/gcm/send'
GCM_CLIENT_KEY = [ 'YOUR DEVICES GCM ID' ]


# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 60
GCM_NOTI_INTERVAL		= 60

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
				'22': Adafruit_DHT.DHT22,
				'2302': Adafruit_DHT.AM2302 }

# Functions!
worksheet = None

def noti_server(temp, humi, msg):
	c = httplib.HTTPSConnection(GCM_REQUEST_URL)
	headers = {}
	headers['Content-Type'] = 'application/json'
	headers['Authorization'] = 'key=' + GCM_SERVER_API_KEY

	notipayload = {'message' : msg + "(Temp={0:0.1f}*C/Humi={1:0.1f}%)".format(temp, humi), 'temp' : temp, 'humi' : humi}
	notimsg = {'registration_ids': GCM_CLIENT_KEY, 'data' : notipayload}
	c.request("POST", GCM_REQUEST_SUBPATH, json.dumps(notimsg), headers)
	response = c.getresponse()
	print response.status, response.reason
	data = response.read()
	print data

# Starts Here!!!

if len(sys.argv) == 7 and sys.argv[1] in sensor_args:
	sensor = sensor_args[sys.argv[1]]
	pin = sys.argv[2]
	temp_low = int(sys.argv[3])
	temp_high = int(sys.argv[4])
	humi_low = int(sys.argv[5])
	humi_high = int(sys.argv[6])
else:
	print 'usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin# [low temperature] [high temperature] [low humidity] [high humidity]'
	print 'example: sudo ./Adafruit_DHT.py 2302 4 23 25 45 60 - Read from an AM2302 connected to GPIO #4'
	sys.exit(1)
		
# For GCM notification
noticount = GCM_NOTI_INTERVAL

# Loop forever!
while True:
	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	
	# Note that sometimes you won't get a reading and
	# the results will be null (because Linux can't
	# guarantee the timing of calls to read the sensor).
	# If this happens try again!
	if humidity is not None and temperature is not None:
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
		is_temp = None
		is_humi = None
		if temperature < temp_low:
			message = 'The room too cold. Shut the window and heat the room!'
			is_temp = "Hot"
		elif temperature > temp_high:
			message = 'The room too hot. Open the window and cool the room!'
			is_temp = "Cold"
		if humidity < humi_low:
			message = message + "/" + 'The room is too dry. Turn the humidifier on!'
			is_humi = "Dry"
		elif humidity > humi_low:
			message = message + "/" + 'The roo is too humid. Turn the humidifier off!'
			is_humi = "Humid"
		if message is not None:
			print message

		if is_temp is not None and is_humi is not None:
			noticount = noticount + 1
			if noticount >= GCM_NOTI_INTERVAL:
				noti_server(temperature, humidity, message)
				noticount = 0
		elif is_temp is None and is_humi is not None:
			noticount = noticount + 1
			if noticount >= GCM_NOTI_INTERVAL:
				noti_server(temperature, humidity, message)
				noticount = 0
		elif is_temp is not None and is_humi is None:
			noticount = noticount + 1
			if noticount >= GCM_NOTI_INTERVAL:
				noti_server(temperature, humidity, message)
				noticount = 0
	else:
		print 'Failed to get reading. Try again!'
	time.sleep(FREQUENCY_SECONDS)
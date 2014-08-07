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
import platform

# Platform identification constants.
UNKNOWN          = 0
RASPBERRY_PI     = 1
BEAGLEBONE_BLACK = 2


def platform_detect(plat=platform.platform()):
	"""Detect if running on the Raspberry Pi or Beaglebone Black and return the
	platform type.  Will return RASPBERRY_PI, BEAGLEBONE_BLACK, or UNKNOWN."""
	# Handle Raspberry Pi
	# Platform output on Raspbian testing/jessie ~May 2014:
	# Linux-3.10.25+-armv6l-with-debian-7.4
	if plat.lower().find('armv6l-with-debian') > -1:
		return RASPBERRY_PI
	# Handle pidora distribution.
	elif plat.lower().find('raspberry_pi') > -1:
		return RASPBERRY_PI
	# Handle arch distribution.
	elif plat.lower().find('arch-armv6l') > -1:
		return RASPBERRY_PI
	# Handle Beaglebone Black
	# Platform output on Debian ~May 2014:
	# Linux-3.8.13-bone47-armv7l-with-debian-7.4
	elif plat.lower().find('armv7l-with-debian') > -1:
		return BEAGLEBONE_BLACK
	# Handle Beaglebone Black
	# Platform output on Ubuntu ~July 2014:
	# Linux-3.8.13-bone56-armv7l-with-Ubuntu-14.04-trusty
	elif plat.lower().find('armv7l-with-ubuntu') > -1:
		return BEAGLEBONE_BLACK	
	elif plat.lower().find('armv7l-with-glibc2.4') > -1:
		return BEAGLEBONE_BLACK
	else:
		return UNKNOWN

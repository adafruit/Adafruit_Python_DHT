Adafruit Python DHT Sensor Library
==================================

Python library to read the DHT series of humidity and temperature sensors on a Raspberry Pi or Beaglebone Black.

Designed specifically to work with the Adafruit DHT series sensors ----> https://www.adafruit.com/products/385

Currently the library is tested with Python 2.6, 2.7, 3.3 and 3.4. It should work with Python greater than 3.4, too.

Installing
----------

For all platforms (Raspberry Pi and Beaglebone Black) make sure your system is able to compile Python extensions.  On Raspbian or Beaglebone Black's Debian/Ubuntu image you can ensure your system is ready by executing:

````
sudo apt-get update
sudo apt-get install build-essential python-dev python3-dev
````

Next, use `pip` to install from PyPI.  For Python2:

```sh
sudo python -m pip install --upgrade pip setuptools wheel
sudo pip install Adafruit_DHT
```

Or for Python 3:

```sh
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
```

Alternatively, you can install from this repository.

For Python 2, install the library by downloading from the [GitHub releases
page](https://github.com/adafruit/Adafruit_Python_DHT/releases),
unzipping the archive, and executing:

```sh
sudo python -m pip install --upgrade pip setuptools wheel
cd Adafruit_Python_DHT
sudo python setup.py install
```

For Python 3, download and extract the library and execute:

```sh
sudo python3 -m pip3 install --upgrade pip setuptools wheel
cd Adafruit_Python_DHT
sudo python3 setup.py install
```

Usage
-----

See example of usage in the examples folder.

Author
------

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Written by Tony DiCola for Adafruit Industries.

MIT license, all text above must be included in any redistribution

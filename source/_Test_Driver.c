// Copyright (c) 2014 Adafruit Industries
// Author: Tony DiCola

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
#include <Python.h>

#include "Test/test_dht_read.h"

// Wrap calling dht_read function and expose it as a DHT.read Python module & function.
static PyObject* Test_Driver_read(PyObject *self, PyObject *args)
{
	// Parse sensor and pin integer arguments.
    int sensor, pin;
    if (!PyArg_ParseTuple(args, "ii", &sensor, &pin)) {
        return NULL;
    }
    // Call dht_read and return result code, humidity, and temperature.
    float humidity = 0, temperature = 0;
    int result = test_dht_read(sensor, pin, &humidity, &temperature);
    return Py_BuildValue("iff", result, humidity, temperature);
}

// Boilerplate python module method list and initialization functions below.

static PyMethodDef module_methods[] = {
    {"read", Test_Driver_read, METH_VARARGS, "Mock DHT read function."},
    {NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
	PyModuleDef_HEAD_INIT,
	"Test_Driver",
	"Adafruit_Python_DHT.Test",
	-1,
	module_methods,
	NULL,
	NULL,
	NULL,
	NULL,
};
#endif

#if PY_MAJOR_VERSION >= 3
PyMODINIT_FUNC PyInit_Test_Driver(void)
#else
PyMODINIT_FUNC initTest_Driver(void)
#endif

{
#if PY_MAJOR_VERSION >= 3
	PyObject * m = PyModule_Create(&moduledef);
#else
	Py_InitModule("Test_Driver", module_methods);
#endif

#if PY_MAJOR_VERSION >= 3
	if (m == NULL)
		return NULL;
	else
		return m;
#endif
}
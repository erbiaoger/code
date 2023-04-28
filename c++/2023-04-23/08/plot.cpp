#include <Python.h>
#include <iostream>

int main()
{
    Py_Initialize();

    PyObject* matplotlib = PyImport_ImportModule("matplotlib.pyplot");
    if (!matplotlib) {
        std::cerr << "Failed to import matplotlib.pyplot\n";
    }

    PyObject* x = PyList_New(5);
    for (size_t i = 0; i < 5; i++) {
        PyList_SetItem(x, i, PyFloat_FromDouble(i));
    }

    PyObject* y = PyList_New(5);
    PyList_SetItem(y, 0, PyFloat_FromDouble(1));
    PyList_SetItem(y, 1, PyFloat_FromDouble(2));
    PyList_SetItem(y, 2, PyFloat_FromDouble(3));
    PyList_SetItem(y, 3, PyFloat_FromDouble(2));
    PyList_SetItem(y, 4, PyFloat_FromDouble(1));

    PyObject* args = PyTuple_New(2);
    PyTuple_SetItem(args, 0, x);
    PyTuple_SetItem(args, 1, y);

    PyObject* title = PyUnicode_FromString("My plot");
    PyObject* kwargs = Py_BuildValue("{s:O}", "label", title);

    PyObject* result = PyObject_CallMethod(matplotlib, "plot", "O{ss}", args, "r", "o", kwargs);
    PyObject* result1 = PyObject_CallMethod(matplotlib, "savefig", "{s}", "a.png");
    Py_XDECREF(result);
    Py_XDECREF(result1);

    Py_DECREF(kwargs);
    Py_DECREF(title);
    Py_XDECREF(args);
    Py_XDECREF(y);
    Py_XDECREF(x);
    Py_XDECREF(matplotlib);

    Py_Finalize();

    return 0;
}

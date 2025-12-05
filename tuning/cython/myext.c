#include <Python.h>

static PyObject* fast_sum(PyObject* self, PyObject* args) {
    PyObject* list;
    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &list))
        return NULL;

    long long total = 0;

    Py_ssize_t size = PyList_Size(list);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject* item = PyList_GetItem(list, i);
        total += PyLong_AsLong(item);
    }

    return PyLong_FromLongLong(total);
}

static PyMethodDef Methods[] = {
    {"fast_sum", fast_sum, METH_VARARGS, "Fast sum of Python list"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "myext",
    NULL,
    -1,
    Methods
};

PyMODINIT_FUNC PyInit_myext(void) {
    return PyModule_Create(&module);
}

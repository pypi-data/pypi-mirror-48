#include <Python.h>

PyMethodDef module_methods[] = {
    {NULL},
};

PyModuleDef module_def = {PyModuleDef_HEAD_INIT, "gym_drone_landing.core", NULL, -1, module_methods};

extern "C" PyObject * PyInit_core() {
    PyObject * module = PyModule_Create(&module_def);
    return module;
}

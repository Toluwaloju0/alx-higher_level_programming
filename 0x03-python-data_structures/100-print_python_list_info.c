#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t list_size = PyList_Size(p);
    Py_ssize_t a;
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    PyObject *item, *type, *name, *str, *encoded;
    char *item_type;

    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %zd\n", allocated);

    for (a = 0; a < list_size; a++) {
        item = PyList_GetItem(p, a);
        if (item == NULL) {
            printf("Error getting item at index %ld\n", a);
            continue;
        }

        type = PyObject_Type(item);
        if (type == NULL) {
            printf("Error getting type of item at index %ld\n", a);
            continue;
        }

        name = PyObject_GetAttrString(type, "__name__");
        if (name == NULL) {
            printf("Error getting name attribute of type at index %ld\n", a);
            Py_DECREF(type);
            continue;
        }

        str = PyObject_Str(name);
        if (str == NULL) {
            printf("Error converting name to string at index %ld\n", a);
            Py_DECREF(type);
            Py_DECREF(name);
            continue;
        }

        encoded = PyUnicode_AsEncodedString(str, "utf-8", "strict");
        if (encoded == NULL) {
            printf("Error encoding string at index %ld\n", a);
            Py_DECREF(type);
            Py_DECREF(name);
            Py_DECREF(str);
            continue;
        }

        item_type = PyBytes_AsString(encoded);
        printf("Element %ld: %s\n", a, item_type);

        Py_DECREF(encoded); // Decrement the reference count of the encoded string
        Py_DECREF(str); // Decrement the reference count of the string object
        Py_DECREF(name); // Decrement the reference count of the name object
        Py_DECREF(type); // Decrement the reference count of the type object
    }
}

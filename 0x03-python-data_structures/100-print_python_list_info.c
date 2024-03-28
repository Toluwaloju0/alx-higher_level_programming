#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)

{
	Py_ssize_t list_size = PyList_Size(p);
	Py_ssize_t a;
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyObject *item;
	char *item_type;


	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %zd\n", allocated);

	for (a = 0; a < list_size; a++)
	{
		item = PyList_GetItem(p, a);
		item = PyObject_Type(item);
		item = PyObject_GetAttrString(item, "__name__");
		item = PyObject_Str(item);
		item = PyUnicode_AsEncodedString(item, "utf-8", "strict");
		item_type = PyBytes_AsString(item);
		printf("Element %ld: %s\n", a, item_type);
	}
}

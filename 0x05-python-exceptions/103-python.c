#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p)
{
if (!PyList_Check(p))
{
printf("[*] Python list info\n");
printf("  [ERROR] Invalid List Object\n");
return;
}

Py_ssize_t list_size = PyList_Size(p);
Py_ssize_t list_alloc = ((PyListObject *)p)->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", list_size);
printf("[*] Allocated = %ld\n", list_alloc);

for (Py_ssize_t index = 0; index < list_size; index++)
{
PyObject *item = PyList_GetItem(p, index);
const char *item_type = Py_TYPE(item)->tp_name;
printf("Element %ld: %s\n", index, item_type);
}
}

void print_python_bytes(PyObject *p)
{
if (!PyBytes_Check(p))
{
printf("[.] bytes object info\n");
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

Py_ssize_t bytes_size = PyBytes_GET_SIZE(p);
const char *bytes_data = PyBytes_AsString(p);

printf("[.] bytes object info\n");
printf("  size: %ld\n", bytes_size);
printf("  trying string: %s\n", bytes_data);

printf("  first %ld bytes: ", (bytes_size > 10) ? 10 : bytes_size);

for (Py_ssize_t i = 0; i < ((bytes_size > 10) ? 10 : bytes_size); i++)
{
printf("%02hhx", bytes_data[i]);

if (i == ((bytes_size > 10) ? 9 : bytes_size - 1))
printf("\n");
else
printf(" ");
}
}

void print_python_float(PyObject *p)
{
if (!PyFloat_Check(p))
{
printf("[.] float object info\n");
printf("  [ERROR] Invalid Float Object\n");
return;
}

double float_val = PyFloat_AS_DOUBLE(p);
printf("[.] float object info\n");
printf("  value: %f\n", float_val);
}

#include <Python.h>

void print_info_about_python_list(PyObject *p);
void print_info_about_python_bytes(PyObject *p);
void print_info_about_python_float(PyObject *p);

void print_info_about_python_list(PyObject *p)
{
Py_ssize_t list_size, list_alloc, i;
const char *type;

PyListObject *list_object = (PyListObject *)p;
PyVarObject *var_object = (PyVarObject *)p;

list_size = var_object->ob_size;
list_alloc = list_object->allocated;

fflush(stdout);

printf("[*] Python list information\n");

if (strcmp(p->ob_type->tp_name, "list") != 0)
{
printf("  [ERROR] Invalid List Object\n");
return;
}

printf("[*] Size of the Python List = %ld\n", list_size);
printf("[*] Allocated = %ld\n", list_alloc);

for (i = 0; i < list_size; i++)
{
type = list_object->ob_item[i]->ob_type->tp_name;
printf("Element %ld: %s\n", i, type);

if (strcmp(type, "bytes") == 0)
print_info_about_python_bytes(list_object->ob_item[i]);
else if (strcmp(type, "float") == 0)
print_info_about_python_float(list_object->ob_item[i]);
}
}

void print_info_about_python_bytes(PyObject *p)
{
Py_ssize_t bytes_size, i;
PyBytesObject *bytes_object = (PyBytesObject *)p;

fflush(stdout);

printf("[.] bytes object information\n");

if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  trying string: %s\n", bytes_object->ob_sval);

bytes_size = (((PyVarObject *)p)->ob_size >= 10) ? 10 : ((PyVarObject *)p)->ob_size + 1;

printf("  first %ld bytes: ", bytes_size);

for (i = 0; i < bytes_size; i++)
{
printf("%02hhx", bytes_object->ob_sval[i]);

if (i == (bytes_size - 1))
printf("\n");
else
printf(" ");
}
}

void print_info_about_python_float(PyObject *p)
{
char *buffer = NULL;
PyFloatObject *float_object = (PyFloatObject *)p;

fflush(stdout);

printf("[.] float object information\n");

if (strcmp(p->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

buffer = PyOS_double_to_string(float_object->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
printf("  value: %s\n", buffer);
PyMem_Free(buffer);
}

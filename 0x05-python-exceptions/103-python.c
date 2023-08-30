#include <Python.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: A PyObject pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
Py_ssize_t list_size, list_alloc, index;
const char *item_type;

PyListObject *list = (PyListObject *)p;
PyVarObject *var = (PyVarObject *)p;

list_size = var->ob_size;
list_alloc = list->allocated;

fflush(stdout);
printf("[*] Python list info\n");

if (strcmp(p->ob_type->tp_name, "list") != 0)
{
printf("  [ERROR] Invalid List Object\n");
return;
}

printf("[*] Size of the Python List = %ld\n", list_size);
printf("[*] Allocated = %ld\n", list_alloc);

for (index = 0; index < list_size; index++)
{
item_type = list->ob_item[index]->ob_type->tp_name;
printf("Element %ld: %s\n", index, item_type);
}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A PyObject pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t bytes_size, i;
PyBytesObject *bytes = (PyBytesObject *)p;

fflush(stdout);
printf("[.] bytes object info\n");

if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

bytes_size = ((PyVarObject *)p)->ob_size;

printf("  size: %ld\n", bytes_size);
printf("  trying string: %s\n", bytes->ob_sval);

printf("  first %ld bytes: ", bytes_size > 10 ? 10 : bytes_size);

for (i = 0; i < bytes_size && i < 10; i++)
{
printf("%02hhx", bytes->ob_sval[i]);

if (i == (bytes_size - 1) || i == 9)
printf("\n");
else
printf(" ");
}
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: A PyObject pointer to the Python float object
 */
void print_python_float(PyObject *p)
{
char *buffer = NULL;
PyFloatObject *float_val = (PyFloatObject *)p;

fflush(stdout);
printf("[.] float object info\n");

if (strcmp(p->ob_type->tp_name, "float") != 0)
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

buffer = PyOS_double_to_string(float_val->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
printf("  value: %s\n", buffer);
PyMem_Free(buffer);
}


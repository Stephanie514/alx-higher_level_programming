#include <stdio.h>
#include <time.h>
#include <Python.h>
/**
 * print_python_bytes - This Prints the bytes info
 *
 * @p: The Python Object
 * Return: 0
 */
void print_python_bytes(PyObject *p)
{
char *byte_string;
long int byte_size, i, limit;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

byte_size = ((PyVarObject *)(p))->ob_size;
byte_string = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", byte_size);
printf("  trying string: %s\n", byte_string);

limit = (byte_size >= 10) ? 10 : byte_size + 1;
printf("  first %ld bytes:", limit);

for (i = 0; i < limit; i++)
{
unsigned char byte_value = (unsigned char)byte_string[i];
printf(" %02x", byte_value);
}

printf("\n");
}

/**
 * print_python_list - This Prints the list info
 *
 * @p: The Python Object
 * Return: 0
 */
void print_python_list(PyObject *p)
{
long int list_size, i;
PyListObject *py_list;
PyObject *element;

list_size = ((PyVarObject *)(p))->ob_size;
py_list = (PyListObject *)p;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", list_size);
printf("[*] Allocated = %ld\n", py_list->allocated);

for (i = 0; i < list_size; i++)
{
element = py_list->ob_item[i];
printf("Element %ld: %s\n", i, ((element)->ob_type)->tp_name);

if (PyBytes_Check(element))
print_python_bytes(element);
}
}

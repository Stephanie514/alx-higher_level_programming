#include <Python.h>

/**
* print_python_list_info - this prints the basic info about Python lists.
* @list_obj: A PyObject list.
*/
void print_python_list_info(PyObject *list_obj)
{
int list_size = Py_SIZE(list_obj);
int list_alloc = ((PyListObject *)list_obj)->allocated;

printf("[*] Size of the Python List = %d\n", list_size);
printf("[*] Allocated = %d\n", list_alloc);

for (int index = 0; index < list_size; index++)
{
PyObject *element = PyList_GetItem(list_obj, index);

printf("Element %d: %s\n", index, Py_TYPE(element)->tp_name);
}
}

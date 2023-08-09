#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
listint_t *walker = list;
listint_t *runner = list;
if (!list)
return (0);

for (; walker && runner && runner->next;)
{
walker = walker->next;
runner = runner->next->next;
if (walker == runner)
return (1);
}
return (0);
}

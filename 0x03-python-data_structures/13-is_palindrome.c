/*
* File: 13-is_palindrome.c
* Auth: Stephanie
*/

#include "lists.h"

listint_t *custom_reverse_listint(listint_t **start);
/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: A pointer to the head of the linked list.
*
* Return: If the linked list is not a palindrome - 0.
*         If the linked list is a palindrome - 1.
*/
int is_palindrome(listint_t **head)
{
listint_t *tmp, *reversed, *mid;
size_t length = 0, i;

if (*head == NULL || (*head)->next == NULL)
return (1);

tmp = *head;

while (tmp)
{
length++;
tmp = tmp->next;
}

tmp = *head;

for (i = 0; i < (length / 2) - 1; i++)
tmp = tmp->next;

if ((length % 2) == 0 && tmp->n != tmp->next->n)
return (0);

tmp = tmp->next->next;

reversed = custom_reverse_listint(&tmp);
mid = reversed;

tmp = *head;

while (reversed)
{
if (tmp->n != reversed->n)
return (0);

tmp = tmp->next;
reversed = reversed->next;
}

custom_reverse_listint(&mid);

return (1);
}
/**
* custom_reverse_listint - Reverses a singly-linked listint_t list.
* @start: A pointer to the starting node of the list to reverse.
*
* Return: A pointer to the head of the reversed list.
*/
listint_t *custom_reverse_listint(listint_t **start)
{
listint_t *current = *start, *next = NULL, *prev = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*start = prev;
return (*start);
}


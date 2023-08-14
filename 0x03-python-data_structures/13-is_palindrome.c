#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;
while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}
*head = prev;
return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev_slow = NULL;
listint_t *second_half, *mid_node = NULL;
int is_palindrome = 1;
if (*head == NULL || (*head)->next == NULL)
return (1);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}
if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}
second_half = slow;
prev_slow->next = NULL;
reverse_listint(&second_half);
listint_t *first_half = *head, *reversed_half = second_half;
while (first_half != NULL && reversed_half != NULL)
{
if (first_half->n != reversed_half->n)
{
is_palindrome = 0;
break;
}
first_half = first_half->next;
reversed_half = reversed_half->next;
}
reverse_listint(&second_half);
if (mid_node != NULL)
{
prev_slow->next = mid_node;
mid_node->next = second_half;
}
else
{
prev_slow->next = second_half;
}
return (is_palindrome);
}

#include "lists.h"
#include <stddef.h>

/**
 * reverse_list - Reverses a singly-linked list.
 * @head: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

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
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *slow_ptr = *head, *fast_ptr = *head, *prev_slow = *head;
	listint_t *second_half, *mid_node = NULL;
	int is_palindrome = 1;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_slow = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	if (fast_ptr != NULL)
	{
		mid_node = slow_ptr;
		slow_ptr = slow_ptr->next;
	}

	second_half = slow_ptr;
	prev_slow->next = NULL;
	reverse_list(&second_half);
	listint_t *first_half = *head, *reversed_half = second_half;

	for (; first_half != NULL && reversed_half != NULL;
			first_half = first_half->next, reversed_half = reversed_half->next)
	{
		if (first_half->n != reversed_half->n)
		{
			is_palindrome = 0;
			break;
		}
	}
	reverse_list(&second_half);
	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	else
	prev_slow->next = second_half;
	return (is_palindrome);
}

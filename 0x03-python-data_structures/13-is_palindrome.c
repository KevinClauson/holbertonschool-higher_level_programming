#include "lists.h"
/**
 * length - gets length of linked list.
 * @head: head of linked list
 * Return: the length of the list.
 */
int length(listint_t *head)
{
	int i;

	i = 0;
	while (head)
	{
		head = head->next;
		++i;
	}
	return (i);
}
/**
 * is_palindrome - checks if linked list is palidrome.
 * @head: pointer to head of linked list
 * Return: 1 if it is palindrome and 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *start, *check;
	int i, j, len, half;

	if (head == NULL)
		return (1);
	if (*head == NULL)
		return (1);
	start = check = *head;
	len = length(*head);
	if (len == 1)
		return (1);
	half = len / 2;

	for (i = 0; i < half; ++i)
	{
		check = *head;
		for (j = 0; j < len - 1; ++j)
		{
			check = check->next;
		}
		if (check->n != start->n)
			return (0);
		--len;
		start = start->next;
	}
	return (1);
}

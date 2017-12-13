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
	listint_t *start;
	int i, j, len;
	int arr[5000];
	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	start = *head;
	len = length(*head);
	/*arr = malloc(sizeof(int) * len);
	if (arr == NULL)
		return (1);
	*/
	i = 0;
	while (start)
	{
		arr[i] = start->n;
		start = start->next;
		++i;
	}
	for (i = 0, j = len - 1; i < j; ++i, --j)
	{
		if (arr[i] != arr[j])
		{
		    return (0);
		}
	}
	return (1);
}

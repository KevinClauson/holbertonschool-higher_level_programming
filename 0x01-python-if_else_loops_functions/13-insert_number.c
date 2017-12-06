#include "lists.h"
/**
 * insert_node - inserts a node into a sorted linked list
 * @head: linked list head
 * @number: number to insert
 * Return: address of new node or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_p, *next_p, *new;

	current_p = next_p = *head;
	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (current_p->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}

	current_p = next_p = *head;

	while(next_p->n < number && next_p)
	{
		current_p = next_p;
		next_p = next_p->next;
	}
	new->next = next_p;
	current_p->next = new;
	return (new);
}

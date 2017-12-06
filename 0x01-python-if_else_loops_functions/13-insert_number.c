#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_p, *next_p, *new;

	if (head == NULL)
		return NULL;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	current_p = next_p = *head;
	next_p = next_p->next;
	if (current_p->n > number)
	{
		*head = new;
		new->next = next_p;
		return (new);
	}
	if (new->n < next_p->n)
	{
		current_p->next = new;
		new->next = next_p;
		return (new);
	}
	while(next_p->n < number && next_p)
	{
		current_p = current_p->next;
		next_p = next_p->next;
	}
	current_p->next = new;
	new->next = next_p;
	return (new);
}

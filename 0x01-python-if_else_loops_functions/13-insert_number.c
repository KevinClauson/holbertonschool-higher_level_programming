#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_p, *next_p, *new;

	if (head == NULL)
		return NULL;
	current_p = next_p = *head;
	next_p = next_p->next;
	while(next_p->n < number && next_p)
	{
		current_p = current_p->next;
		next_p = next_p->next;
	}
	if (next_p == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t) * 1);
	new->n = number;
	current_p->next = new;
	new->next = next_p;
	return (new);
}

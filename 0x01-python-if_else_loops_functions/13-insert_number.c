#include "lists.h"
/**
 * insert_node - inserts a node into a sorted linked list
 * @head: linked list head
 * @number: number to insert
 * Return: address of new node or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_n, *prior_n, *new;

	prior_n = NULL;
	current_n = *head;
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
	if (current_n->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}

	while(current_n && current_n->n < number)
	{
		prior_n = current_n;
		current_n = current_n->next;
	}
	new->next = current_n;
	prior_n->next = new;
	return (new);
}

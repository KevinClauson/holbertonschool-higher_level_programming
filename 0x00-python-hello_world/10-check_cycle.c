#include "lists.h"
/**
 * check_cycle - check to see if linked list has a cycle or not.
 * @list: head of linked list.
 * Return: 1 if there is a cycle and 0 if no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *step_1, *step_2;
	if (list == NULL)
		return (0);
	step_1 = list;
	step_2 = list->next;

	while(step_1 != step_2 && step_2 != NULL)
	{
		step_1 = step_1->next;
		step_2 = step_2->next;
		if(step_2 == NULL)
			break;
		step_2 = step_2->next;
	}
	if (step_1 == step_2)
		return (1);
        else
		return (0);
}

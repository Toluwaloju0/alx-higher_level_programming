#include "lists.h"

/**
* check_cycle - to check if a linked list has a cycle
* @list: pointer to the head of a linked list
* Return: 1 if cycle, 0 if no cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *h = list, *check = list;

	while (h->next != NULL)
	{
		if (h->next == check)
		{
			return (1);
		}
		h = h->next;
	}
	return (0);
}

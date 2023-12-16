#include "lists.h"

/**
* check_cycle - to check if a linked list has a cycle
* @list: pointer to the head of a linked list
* Return: 1 if cycle, 0 if no cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *h = list, *check = list, *hare = list;

	if (list == NULL)
	{
		return (0);
	}
	while (h->next != NULL)
	{
		if (h->next == check)
		{
			return (1);
		}
		h = h->next;
		hare = hare->next->next;
		if (h == hare)
		{
			return(1);
		}
	}
	return (0);
}

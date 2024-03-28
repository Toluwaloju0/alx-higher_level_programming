#include "lists.h"

/**
* is_palindrome - to check if a list is empty
* @head: pointer to the list
* Return: 1 if empty, 0 if not empty
*/

int is_palindrome(listint_t **head)
{
	listint_t *h, *a;

	if (head == NULL)
	{
		return(1);
	}

	h = *head;
	a = *head;
	while (h != NULL)
	{
		while (a != NULL)
		{
			if (h->n == a-> n)
			{
				break;
			}
			else
			{
				return (1);
			}
			a = a->next;
		}
		h = h->next;
	}
	return(0);
}

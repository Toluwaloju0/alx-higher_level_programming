#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - to add a node to a sorted linked list
 * @head: the beginning of the node
 * @number: the number to be included
 * Return: A pinter to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head, *new, *i;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (h->n > number)
	{
		new->next = h;
		return (new);
	}
	while (h->next != NULL)
	{
		if (h->next->n > number)
		{
			i = h->next;
			h->next = new;
			new->next = i;
			return (new);
		}
		h = h->next;
	}
	if (h->n < number)
	{
		h->next = new;
		return (new);
	}
	return (NULL);
}

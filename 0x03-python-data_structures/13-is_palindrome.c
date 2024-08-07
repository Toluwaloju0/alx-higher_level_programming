#include "lists.h"
#include <stdio.h>

/**
 * l_size - to find the lingth of a linked list
 * @head: the lined list head
 * Return: the number of nodes in a linked list
 */

int l_size(listint_t **head)
{
	listint_t *h = *head;
	int a = 0;

	while (h != NULL)
	{
		h = h->next;
		a++;
	}
	return (a);
}

/**
* is_palindrome - to check if a list is empty
* @head: pointer to the list
* Return: 1 if palindrome, 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *h, *a;
	int len, b;

	if (head == NULL)
	{
		return (0);
	}

	h = *head;
	len = l_size(head);
	if (len == 1)
	{
		return (1);
	}
	while (h)
	{
		a = *head;
		b = 0;
		while (b < len - 1)
		{
			a = a->next;
			b++;
		}
		if (h->n == a->n)
		{
			h = h->next;
			len--;
			continue;
		}
		else
		{
			return (0);
		}
		h = h->next;
		len--;
	}
	return (1);
}

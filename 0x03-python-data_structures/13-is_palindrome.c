#include "lists.h"

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
* Return: 1 if empty, 0 if not empty
*/

int is_palindrome(listint_t **head)
{
	listint_t *h, *a;
	int len, b;

	if (head == NULL)
	{
		return (1);
	}

	h = *head;
	len = l_size(head);
	if (len == 1)
	{
		return (0);
	}
	while (h != NULL)
	{
		a = *head;
		b = 0;
		while (b < len)
		{
			if (h->n == a->n)
			{
				a = a->next;
				b++;
				continue;
			}
			else
			{
				return (1);
			}
			a = a->next;
			b++;
		}
		h = h->next;
		len--;
	}
	return (0);
}

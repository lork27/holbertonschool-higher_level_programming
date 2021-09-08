#include "lists.h"
#include <stdlib.h>
/**
 *insert_node - insterts node into sorted linked list
 *@head: pointer to the pointer of the linked list
 *@number: number to be inserted to that new node
 *Return: addres of new node or null if fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *new = NULL;

	if (number == NULL)
		return (NULL);

	while (tmp->next != NULL)
	{
		if (number > tmp->n && number < tmp->next->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (NULL);
}

#include "lists.h"
/**
 *check_cycle - checks if a singly link list has a cycle
 *@list: linked list to be checked
 *Return: 0 if no cycle 1 if yes
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	fast = list->next, slow = list;

	while (fast->next != NULL)
	{
		slow = slow;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}

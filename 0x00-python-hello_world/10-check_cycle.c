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
	fast = list->next;
	slow = list;
	while (slow && fast && fast->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

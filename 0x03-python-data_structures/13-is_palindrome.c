#include "lists.h"

/**
 * reverse - Reverses singly linked list
 * @list : list to reverse
 * Return : Reversed list
 */

listint_s reverse(listint_s *list)
{
	listint_s *new_list = NULL;

	if (list == NULL)
		return NULL;

	if (!list->next)
	{
		add_nodeint_end(&new_list, list->n);
		return (new_list);
	}

	new_list = reverse_list(list->next);
	add_nodeint_end(&new_list, list->n);

	return (new_list);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to first linked list
 * Return: 1 if palindrome 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = NULL, *reversed = NULL, *my_list = *head;

	if (*head == NULL)
		return (1);

	reversed = reverse_list(my_list);
	tmp = reversed;


	while (my_list)
	{
		if (my_list->n != reversed->n)
		{
			free_listint(tmp);
			return (0);
		}
		my_list = my_list->next;
		reversed = reversed->next;
	}

	free_listint(tmp);
	return (1);
}

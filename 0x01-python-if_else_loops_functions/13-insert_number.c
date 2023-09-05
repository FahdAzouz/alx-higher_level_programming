#include "lists.h"

/**
 * insert_node - inserts a new node
 * @head: head
 * @number: number of new node
 * Return: the address of the new node, or NULL if it
 * failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;
	listint_t *nhead;
	listint_t *h_prev;

	nhead = *head;
	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
		return (NULL);

	while (nhead != NULL)
	{
		if (head->n > number)
			break;
		h_prev = nhead;
		nhead = nhead->next;
	}

	newnode->n = number;

	if (*head == NULL)
	{
		newnode->next = NULL;
		*head = newnode;
	}
	else
	{
		newnode->next = nhead;
		if (nhead == *head)
			*head = newnode;
		else
			h_prev->next = newnode;
	}

	return (newnode);
}

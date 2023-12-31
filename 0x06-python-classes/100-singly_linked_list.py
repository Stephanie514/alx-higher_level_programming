#!/usr/bin/python3

"""Define class Node"""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.my_data = data
        self.my_next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.my_data

    @data.setter
    def data(self, value):
        """Set the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.my_data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.my_next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the Node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.my_next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__my_head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)

        if self.__my_head is None:
            new_node.next_node = None
            self.__my_head = new_node
        elif self.__my_head.data > value:
            new_node.next_node = self.__my_head
            self.__my_head = new_node
        else:
            tmp = self.__my_head
            while (tmp.next_node is not None and
                   tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__my_head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    values = [5, 2, 8, 1, 9, 3]
    for val in values:
        linked_list.sorted_insert(val)
    print(linked_list)

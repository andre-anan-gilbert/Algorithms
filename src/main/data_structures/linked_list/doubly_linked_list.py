"""An implementation of a doubly linked list."""
from typing import Generic, Iterator, TypeVar

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    """Class that represents a doubly linked list.

    Attributes:
        _size: The size of the linked list.
        _head: The head of the linked list.
        _tail: The tail of the linked list.
    """

    def __init__(self) -> None:
        self._size = 0
        self._head = None
        self._tail = None

    class _Node(Generic[T]):
        """Internal class node to represent data.

        Attributes:
            data: The data of the node.
            prev: The pointer to the previous node.
            next: The pointer to the next node.
        """

        def __init__(self, data: T, prev_node, next_node) -> None:
            self.data = data
            self.prev = prev_node
            self.next = next_node

        def __str__(self) -> str:
            return str(self.data)

    def clear(self) -> None:
        """Empties the linked list in O(n)."""
        trav = self._head
        while trav is not None:
            next_node = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next_node

        self._head = self._tail = trav = None
        self._size = 0

    def size(self) -> int:
        """Returns the size of the linked list."""
        return self._size

    def is_empty(self) -> bool:
        """Checks if the linked list is empty."""
        return self.size() == 0

    def add(self, elem: T) -> None:
        """Adds an element to the tail of the linked list in O(1)."""
        self.add_last(elem)

    def add_last(self, elem: T) -> None:
        """Adds a node to the tail of the linked list, O(1)."""
        if self.is_empty():
            self._head = self._tail = self._Node(elem, None, None)
        else:
            self._tail.next = self._Node(elem, self._tail, None)
            self._tail = self._tail.next

        self._size += 1

    def add_first(self, elem: T) -> None:
        """Adds an element to the beginning of the linked list, O(1)."""
        if self.is_empty():
            self._head = self._tail = self._Node(elem, None, None)
        else:
            self._head.prev = self._Node(elem, None, self._head)
            self._head = self._head.prev

        self._size += 1

    def add_at(self, index: int, elem: T) -> None:
        """Adds an element at a specified index."""
        if index < 0 or index > self._size: raise IndexError('Illegal index.')

        if index == 0:
            self.add_first(elem)
            return

        if index == self._size:
            self.add_last(elem)
            return

        temp = self._head
        for _ in range(0, index - 1):
            temp = temp.next

        new_node = self._Node(elem, temp, temp.next)
        temp.next.prev = new_node
        temp.next = new_node

        self._size += 1

    def peek_first(self) -> None:
        """Returns the value of the first node if it exists, O(1)."""
        if self.is_empty(): raise RuntimeError('Empty list.')
        return self._head.data

    def peek_last(self) -> T:
        """Returns the value of the last node if it exists, O(1)."""
        if self.is_empty(): raise RuntimeError('Empty list.')
        return self._tail.data

    def remove_first(self) -> T:
        """Removes the first node of the linked list, O(1)."""
        if self.is_empty(): raise RuntimeError('Empty list.')

        data = self._head.data
        self._head = self._head.next
        self._size -= 1

        if self.is_empty():
            self._tail = None
        else:
            self._head.prev = None

        return data

    def remove_last(self) -> T:
        """Removes the last node of the linked list, O(1)."""
        if self.is_empty(): raise RuntimeError('Empty list.')

        data = self._tail.data
        self._tail = self._tail.prev
        self._size -= 1

        if self.is_empty():
            self._head = None
        else:
            self._tail.next = None

        return data

    def _remove(self, node: _Node) -> T:
        """Removes an arbitrary node from the linked list, O(1)."""
        if node.prev is None: return self.remove_first()
        if node.next is None: return self.remove_last()

        node.next.prev = node.prev
        node.prev.next = node.next

        data = node.data
        node.data = node.next = node.prev = None
        node = None

        self._size -= 1

        return data

    def remove_at(self, index: int) -> T:
        """Removes a node at a particular index, O(n)."""
        if index < 0 or index >= self._size: raise IndexError('Illegal index.')

        if index < self._size // 2:
            i = 0
            trav = self._head
            while i != index:
                i += 1
                trav = trav.next

        else:
            i = self._size - 1
            trav = self._tail
            while i != index:
                i -= 1
                trav = trav.prev

        return self._remove(trav)

    def remove(self, obj: object) -> bool:
        """Removes a particular value in the linked list, O(n)."""
        trav = self._head

        # Search for None value
        if obj is None:
            trav = self._head
            while trav is not None:
                if trav.data is None:
                    self._remove(trav)
                    return True

                trav = trav.next

        # Search for non None value
        else:
            trav = self._head
            while trav is not None:
                if obj == trav.data:
                    self._remove(trav)
                    return True

                trav = trav.next

        return False

    def index_of(self, obj: object) -> int:
        """Returns the index of a particular value in the linked list, O(n)."""
        index = 0
        trav = self._head

        # Search for None value
        if obj is None:
            while trav is not None:
                if trav.data is None:
                    return index

                trav = trav.next
                index += 1

        # Search for non None value
        else:
            while trav is not None:
                if obj == trav.data:
                    return index

                trav = trav.next
                index += 1

        return -1

    def contains(self, obj: object) -> bool:
        """Checks if a value exists in the linked list."""
        return self.index_of(obj) != -1

    def __iter__(self) -> Iterator:
        self._iter = self._head
        return self

    def __next__(self) -> T:
        if self._iter is None: raise StopIteration

        data = self._iter.data
        self._iter = self._iter.next

        return data

    def __str__(self) -> str:
        linked_list = '['
        trav = self._head
        while trav is not None:
            linked_list += str(trav.data)
            if trav.next is not None:
                linked_list += ', '

            trav = trav.next

        linked_list += ']'
        return linked_list


def main() -> None:
    linked_list = DoublyLinkedList()
    print(linked_list.is_empty())
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    print(linked_list.is_empty())
    print(linked_list)
    print(linked_list.size())
    print(linked_list.peek_first())
    print(linked_list.peek_last())
    print(linked_list.contains(2))
    linked_list.remove(2)
    linked_list.remove_first()
    linked_list.remove_last()
    linked_list.add(1)
    print(linked_list)


if __name__ == '__main__':
    main()

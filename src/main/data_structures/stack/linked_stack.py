"""An implementation of a stack using a linked list."""
from typing import Generic, Iterator, TypeVar
from collections import deque

T = TypeVar('T')


class LinkedStack(Generic[T]):
    """Class representing a stack.

    Attributes:
        _stack: The linked list stack.
    """

    def __init__(self) -> None:
        self._stack = deque()

    def size(self) -> int:
        """Return the size of the stack."""
        return len(self._stack)

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return self.size() == 0

    def push(self, elem: T) -> None:
        """Adds an element to the stack."""
        self._stack.append(elem)

    def pop(self) -> T:
        """Removes an element from the stack."""
        if self.is_empty(): raise RuntimeError('Empty stack.')
        return self._stack.pop()

    def peek(self) -> T:
        """Returns the top element."""
        if self.is_empty(): raise RuntimeError('Empty stack.')
        return self._stack[-1]

    def __iter__(self) -> Iterator:
        self._iter = iter(self._stack)
        return self

    def __next__(self) -> T:
        return next(self._iter)

    def __str__(self) -> str:
        return str(self._stack)

    def __bool__(self) -> bool:
        return bool(self._stack)

    def __contains__(self, elem: T) -> bool:
        return elem in self._stack


def main() -> None:
    stack = LinkedStack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.is_empty())
    print(stack)
    print(stack.size())
    print(stack.peek())
    print(3 in stack)
    stack.pop()
    print(stack.peek())
    print(3 in stack)


if __name__ == '__main__':
    main()

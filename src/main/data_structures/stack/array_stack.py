"""An implementation of a stack using an array."""
from typing import Generic, TypeVar

T = TypeVar('T')


class ArrayStack:
    """Class representing a stack.

    Attributes:
        _stack: The array stack.
    """

    def __init__(self) -> None:
        """Inits the stack."""
        self._stack = []

    def __str__(self) -> str:
        return str(self._stack)

    def __bool__(self) -> bool:
        return bool(self._stack)

    def __contains__(self, elem: Generic[T]) -> bool:
        return elem in self._stack

    def size(self) -> int:
        """Returns the size of the stack."""
        return len(self._stack)

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return not self._stack

    def push(self, elem: Generic[T]) -> None:
        """Adds an element to the stack."""
        self._stack.append(elem)

    def pop(self) -> Generic[T]:
        """Removes an element from the stack."""
        return self._stack.pop()

    def peek(self) -> Generic[T]:
        """Returns the top element."""
        if self.is_empty(): raise RuntimeError('Empty stack.')
        return self._stack[-1]


def main() -> None:
    stack = ArrayStack()
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

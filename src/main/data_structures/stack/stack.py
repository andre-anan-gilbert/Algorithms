"""Abstract base class for the stacks."""
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Stack(ABC):
    """An abstract base class for the stack implementations."""

    @abstractmethod
    def size(self) -> int:
        """Returns the size of the stack."""
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        pass

    @abstractmethod
    def push(self, elem: Generic[T]) -> None:
        """Adds an element to the stack."""
        pass

    @abstractmethod
    def pop(self) -> Generic[T]:
        """Removes an element from the stack."""
        pass

    @abstractmethod
    def peek(self) -> Generic[T]:
        """Returns the top element."""
        pass

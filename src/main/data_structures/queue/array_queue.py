"""An array implementation of a queue."""
from typing import Generic, TypeVar

T = TypeVar('T')


class ArrayQueue:
    """Class representing a queue.

    Attributes:
        _queue: The array queue.
    """

    def __init__(self) -> None:
        """Inits the queue."""
        self._queue = []

    def __str__(self) -> str:
        return str(self._queue)

    def __bool__(self) -> bool:
        return bool(self._queue)

    def __contains__(self, elem: Generic[T]) -> bool:
        return elem in self._queue

    def size(self) -> int:
        """Returns the size of the queue."""
        return len(self._queue)

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return not self._queue

    def offer(self, elem: Generic[T]) -> None:
        """Adds an element to the end of the queue."""
        self._queue.append(elem)

    def poll(self) -> Generic[T]:
        """Removes the front element of the queue."""
        if self.is_empty(): raise RuntimeError('Queue is empty.')
        return self._queue.pop(0)

    def peek(self) -> Generic[T]:
        """Returns the front element of the queue."""
        if self.is_empty(): raise RuntimeError('Queue is empty.')
        return self._queue[0]


def main() -> None:
    queue = ArrayQueue()
    print(queue.is_empty())
    queue.offer(1)
    queue.offer(2)
    queue.offer(3)
    print(queue.is_empty())
    print(queue)
    print(queue.size())
    print(queue.peek())
    print(1 in queue)
    queue.poll()
    print(queue.peek())
    print(1 in queue)


if __name__ == '__main__':
    main()

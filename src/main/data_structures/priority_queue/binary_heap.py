"""An implementation of a priority queue using a binary heap."""
from typing import Generic, TypeVar

T = TypeVar('T')


class BinaryHeap(Generic[T]):
    """Class that represents a priority queue.

    Attributes:
        _heap: The binary heap priority queue.
    """

    def __init__(self) -> None:
        self._heap = []

    def heapify(self, elems: T) -> None:
        """Construct a priority queue using heapify, O(n)."""
        heap_size = len(elems)

        for i in range(heap_size):
            self._heap.append(elems[i])

        # Heapify the elements
        for i in range(max(0, (heap_size // 2) - 1), -1, -1):
            self._sink(i)

    def size(self) -> int:
        """Return the size of the priority queue."""
        return len(self._heap)

    def is_empty(self) -> bool:
        """Checks if the priority is empty."""
        return self.size() == 0

    def clear(self) -> None:
        """Empties the priority queue."""
        self._heap.clear()

    def peek(self) -> T:
        """Returns the value of the element with the lowest priority."""
        if self.is_empty(): return
        return self._heap[0]

    def poll(self) -> T:
        """Removes the root of the binary heap, O(log(n))."""
        return self.remove_at(0)

    def contains(self, elem: T) -> bool:
        """Checks if an element exists in the priority queue, O(n)."""
        for i in range(self.size()):
            if self._heap[i] == elem:
                return True

        return False

    def add(self, elem: T) -> None:
        """Adds an element to the priority queue, O(log(n))."""
        if elem is None: raise ValueError()

        self._heap.append(elem)

        index_of_last_elem = self.size() - 1
        self._swim(index_of_last_elem)

    def _less(self, i: int, j: int) -> bool:
        """Checks if node i <= node j"""
        node1 = self._heap[i]
        node2 = self._heap[j]
        return node1 <= node2

    def _swim(self, k: int) -> None:
        """Performs a bottom up node swim, O(log(n))."""
        parent = (k - 1) // 2

        # Keep swimming until we have reached the root
        # and while we're less than our parent
        while k > 0 and self._less(k, parent):
            self._swap(k, parent)
            k = parent

            parent = (k - 1) // 2

    def _sink(self, k: int) -> None:
        """Performs a top down node sink, O(log(n))."""
        heap_size = self.size()

        while True:
            left = 2 * k + 1
            right = 2 * k + 2
            smallest = k

            if left < heap_size and self._less(left, smallest):
                smallest = left

            if right < heap_size and self._less(right, smallest):
                smallest = right

            if smallest != k:
                self._swap(smallest, k)
                k = smallest
            else:
                break

    def _swap(self, i: int, j: int) -> None:
        """Swaps two nodes."""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def remove(self, elem: T) -> bool:
        """Removes a particular element in the priority queue, O(n)."""
        if elem is None: return False

        for i in range(self.size()):
            if self._heap[i] == elem:
                self.remove_at(i)
                return True

        return False

    def remove_at(self, i: int) -> T:
        """Removes a node at a particular index, O(log(n))."""
        if self.is_empty(): return

        index_of_last_elem = self.size() - 1
        data = self._heap[i]
        self._swap(i, index_of_last_elem)

        self._heap.pop()

        if i == index_of_last_elem: return data
        elem = self._heap[i]

        self._sink(i)

        if self._heap[i] == elem: self._swim(i)
        return data

    def __str__(self) -> str:
        return str(self._heap)


def main() -> None:
    array = [50, 10, 40, 60, 20]
    binary_heap = BinaryHeap()
    binary_heap.heapify(array)
    print(binary_heap.size())
    print(binary_heap.is_empty())
    print(binary_heap.peek())
    print(binary_heap.contains(30))
    binary_heap.add(0)
    binary_heap.add(30)
    print(binary_heap.peek())
    binary_heap.poll()
    print(binary_heap.peek())
    binary_heap.remove(50)
    print(binary_heap)


if __name__ == '__main__':
    main()

"""An implementation of heapsort - O(n * log(n))."""


class Heapsort:
    """Class that sorts arrays using heapsort."""

    def sort(self, array: list[int]) -> None:
        self._heapsort(array)

    def _heapsort(self, array: list[int]) -> None:
        """Sorts the array using heapsort."""
        if not array: return
        size = len(array)

        # Heapify converts array into binary heap - O(n)
        for i in range(max(0, (size // 2) - 1), -1, -1):
            self._sink(array, size, i)

        for i in range(size - 1, 0, -1):
            self._swap(array, 0, i)
            self._sink(array, i, 0)

    def _sink(self, array: list[int], size: int, i: int) -> None:
        """Maintains the max-heap property of the entire tree."""
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            # Left child is larger than parent
            if left < size and array[left] > array[largest]:
                largest = left

            # Right child is larger than parent
            if right < size and array[right] > array[largest]:
                largest = right

            # Move down the tree following the largest node
            if largest != i:
                self._swap(array, largest, i)
                i = largest
            else:
                break

    def _swap(self, array: list[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]

def main() -> None:
    sorter = Heapsort()
    array = [10, 4, 6, 8, 13, 2, 3]
    sorter.sort(array)
    print(array)


if __name__ == '__main__':
    main()
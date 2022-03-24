"""An implementation of quick sort - O(n * log(n))."""


class QuickSort:
    """Class that sorts arrays using quick sort."""

    def sort(self, array: list[int]) -> None:
        if not array: return
        self._quick_sort(array, 0, len(array) - 1)

    def _quick_sort(self, array: list[int], low: int, high: int) -> None:
        if low < high:
            pivot_index = self._partition(array, low, high)
            self._quick_sort(array, low, pivot_index - 1)
            self._quick_sort(array, pivot_index + 1, high)

    def _partition(self, array: list[int], low: int, high: int) -> None:
        """Partitions the array and returns the pivot index."""
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                self._swap(array, i, j)

        self._swap(array, high, i + 1)
        return i + 1

    def _swap(self, array: list[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]


def main() -> None:
    sorter = QuickSort()
    array = [10, 4, 6, 4, 8, -13, 2, 3]
    sorter.sort(array)
    print(array)


if __name__ == '__main__':
    main()

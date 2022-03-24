"""An implementation of insertion sort - O(n²)."""


class InsertionSort:
    """Class that sorts arrays using insertion sort."""

    def sort(self, array: list[int]) -> None:
        if not array: return
        self._insertion_sort(array)

    def _insertion_sort(self, array: list[int]) -> None:
        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j] < array[j - 1]:
                self._swap(array, j - 1, j)
                j -= 1

    def _swap(self, array: list[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]


def main() -> None:
    sorter = InsertionSort()
    array = [10, 4, 6, 4, 8, -13, 2, 3]
    sorter.sort(array)
    print(array)


if __name__ == '__main__':
    main()

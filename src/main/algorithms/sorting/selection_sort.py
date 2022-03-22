"""An implementation of selection sort - O(n²)."""


class SelectionSort:
    """Class that sorts array using selection sort."""

    def sort(self, array: list[int]) -> None:
        if len(array) <= 1: return
        self._selection_sort(array)

    def _selection_sort(self, array: list[int]) -> None:
        size = len(array)

        for i in range(size):
            swap_index = i
            for j in range(i + 1, size):
                if array[j] < array[swap_index]:
                    swap_index = j

            self._swap(array, i, swap_index)

    def _swap(self, array: list[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]


def main() -> None:
    sorter = SelectionSort()
    array = [10, 4, 6, 4, 8, -13, 2, 3]
    sorter.sort(array)
    print(array)


if __name__ == '__main__':
    main()
"""An implementation of bubble sort - O(n²)."""


class BubbleSort:
    """Class that sorts arrays using bubble sort."""

    def sort(self, array: list[int]) -> None:
        if len(array) <= 1: return
        self._bubble_sort(array)

    def _bubble_sort(self, array: list[int]) -> None:
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(1, len(array)):
                if array[i] < array[i - 1]:
                    self._swap(array, i - 1, i)
                    is_sorted = False

    def _swap(self, array: list[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]


def main() -> None:
    sorter = BubbleSort()
    array = [10, 4, 6, 4, 8, -13, 2, 3]
    sorter.sort(array)
    print(array)


if __name__ == '__main__':
    main()
